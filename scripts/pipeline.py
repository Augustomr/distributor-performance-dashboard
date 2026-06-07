from datetime import datetime
from pathlib import Path
import json
import urllib.request

import pandas as pd

from generate_data import generate_dataset


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"

TREATED_DATASET_PATH = DATA_DIR / "dataset_tratado.csv"
KPI_SUMMARY_PATH = OUTPUT_DIR / "kpis_resumo.csv"
AI_PROMPT_PATH = OUTPUT_DIR / "ai_analysis_prompt.md"

USD_BRL_API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
FALLBACK_USD_BRL = 5.00

COLUMN_RENAMES = {
    "Distributor_ID": "id_distribuidor",
    "Distributor": "distribuidor",
    "Grupo": "grupo",
    "Categoria": "categoria",
    "kpiType": "tipo_kpi",
    "isFocusCategory": "categoria_foco",
    "Meta": "meta_unidades",
    "Realizado": "realizado_unidades",
    "Data": "data",
    "Premiacao": "premiacao_brl",
    "Cobertura": "cobertura_meta",
    "Distributor_Num": "numero_distribuidor",
    "Grupo_Label": "grupo_label",
}

# Regra comercial: quantidade de unidades equivalente a um valor em dolar.
CATEGORY_PRICE_RULES = {
    "CEREAL": {"units": 10, "usd_value": 50.00},
    "CREME DE LEITE": {"units": 10, "usd_value": 35.00},
    "AÇÚCAR": {"units": 10, "usd_value": 25.00},
    "LEITE": {"units": 10, "usd_value": 40.00},
    "CAFÉ": {"units": 10, "usd_value": 80.00},
    "CHOCOLATE": {"units": 10, "usd_value": 70.00},
    "OUTROS": {"units": 10, "usd_value": 30.00},
}


def get_usd_brl_quote():
    try:
        with urllib.request.urlopen(USD_BRL_API_URL, timeout=10) as response:
            payload = json.loads(response.read().decode("utf-8"))

        quote = float(payload["USDBRL"]["bid"])
        return {
            "cotacao": quote,
            "fonte": USD_BRL_API_URL,
            "fallback": False,
            "mensagem": "Cotacao obtida em API publica.",
        }
    except Exception as exc:
        return {
            "cotacao": FALLBACK_USD_BRL,
            "fonte": "fallback_local",
            "fallback": True,
            "mensagem": f"Falha ao consultar API publica. Fallback usado: {exc}",
        }


def prepare_dataset(df, usd_brl_quote):
    df = df.rename(columns=COLUMN_RENAMES).copy()
    df["data"] = pd.to_datetime(df["data"])

    price_table = pd.DataFrame(
        [
            {
                "categoria": category,
                "unidades_regra_preco": rule["units"],
                "valor_regra_usd": rule["usd_value"],
                "valor_unitario_usd": rule["usd_value"] / rule["units"],
            }
            for category, rule in CATEGORY_PRICE_RULES.items()
        ]
    )

    df = df.merge(price_table, on="categoria", how="left")

    missing_prices = sorted(df.loc[df["valor_unitario_usd"].isna(), "categoria"].unique())
    if missing_prices:
        raise ValueError(f"Categorias sem regra de preco: {missing_prices}")

    df["cotacao_dolar_brl"] = round(usd_brl_quote, 4)
    df["valor_meta_usd"] = df["meta_unidades"] * df["valor_unitario_usd"]
    df["valor_realizado_usd"] = df["realizado_unidades"] * df["valor_unitario_usd"]
    df["valor_meta_brl"] = df["valor_meta_usd"] * df["cotacao_dolar_brl"]
    df["valor_realizado_brl"] = df["valor_realizado_usd"] * df["cotacao_dolar_brl"]
    df["diferenca_unidades"] = df["realizado_unidades"] - df["meta_unidades"]
    df["diferenca_valor_brl"] = df["valor_realizado_brl"] - df["valor_meta_brl"]

    df["atingimento_percentual"] = (
        df["realizado_unidades"] / df["meta_unidades"].replace(0, pd.NA) * 100
    ).fillna(0)

    money_columns = [
        "valor_regra_usd",
        "valor_unitario_usd",
        "valor_meta_usd",
        "valor_realizado_usd",
        "valor_meta_brl",
        "valor_realizado_brl",
        "diferenca_valor_brl",
    ]
    df[money_columns] = df[money_columns].round(2)
    df["diferenca_unidades"] = df["diferenca_unidades"].round(2)
    df["atingimento_percentual"] = df["atingimento_percentual"].round(2)

    return df


def build_kpis(df):
    total_meta_units = df["meta_unidades"].sum()
    total_realized_units = df["realizado_unidades"].sum()
    total_meta_brl = df["valor_meta_brl"].sum()
    total_realized_brl = df["valor_realizado_brl"].sum()

    overview = {
        "periodo_inicio": df["data"].min().date().isoformat(),
        "periodo_fim": df["data"].max().date().isoformat(),
        "linhas": len(df),
        "distribuidores": df["id_distribuidor"].nunique(),
        "categorias": df["categoria"].nunique(),
        "meta_unidades": round(total_meta_units, 2),
        "realizado_unidades": round(total_realized_units, 2),
        "atingimento_percentual": round(total_realized_units / total_meta_units * 100, 2),
        "diferenca_unidades": round(total_realized_units - total_meta_units, 2),
        "valor_meta_usd": round(df["valor_meta_usd"].sum(), 2),
        "valor_realizado_usd": round(df["valor_realizado_usd"].sum(), 2),
        "valor_meta_brl": round(total_meta_brl, 2),
        "valor_realizado_brl": round(total_realized_brl, 2),
        "diferenca_valor_brl": round(total_realized_brl - total_meta_brl, 2),
        "cobertura_percentual": round(df["cobertura_meta"].mean() * 100, 2),
        "premiacao_brl": round(df["premiacao_brl"].sum(), 2),
    }

    category_summary = (
        df.groupby("categoria", as_index=False)
        .agg(
            meta_unidades=("meta_unidades", "sum"),
            realizado_unidades=("realizado_unidades", "sum"),
            valor_realizado_usd=("valor_realizado_usd", "sum"),
            valor_realizado_brl=("valor_realizado_brl", "sum"),
            cobertura_percentual=("cobertura_meta", lambda series: series.mean() * 100),
            premiacao_brl=("premiacao_brl", "sum"),
        )
        .assign(
            atingimento_percentual=lambda frame: (
                frame["realizado_unidades"] / frame["meta_unidades"] * 100
            )
        )
        .sort_values("valor_realizado_brl", ascending=False)
    )

    distributor_summary = (
        df.groupby(["id_distribuidor", "distribuidor", "grupo_label"], as_index=False)
        .agg(
            meta_unidades=("meta_unidades", "sum"),
            realizado_unidades=("realizado_unidades", "sum"),
            valor_realizado_brl=("valor_realizado_brl", "sum"),
            cobertura_percentual=("cobertura_meta", lambda series: series.mean() * 100),
            premiacao_brl=("premiacao_brl", "sum"),
        )
        .assign(
            atingimento_percentual=lambda frame: (
                frame["realizado_unidades"] / frame["meta_unidades"] * 100
            )
        )
    )

    group_summary = (
        df.groupby("grupo_label", as_index=False)
        .agg(
            meta_unidades=("meta_unidades", "sum"),
            realizado_unidades=("realizado_unidades", "sum"),
            valor_realizado_brl=("valor_realizado_brl", "sum"),
            cobertura_percentual=("cobertura_meta", lambda series: series.mean() * 100),
            premiacao_brl=("premiacao_brl", "sum"),
        )
        .assign(
            atingimento_percentual=lambda frame: (
                frame["realizado_unidades"] / frame["meta_unidades"] * 100
            )
        )
        .sort_values("valor_realizado_brl", ascending=False)
    )

    top_distributors = distributor_summary.sort_values(
        "valor_realizado_brl", ascending=False
    ).head(10)

    attention_distributors = distributor_summary.sort_values(
        ["atingimento_percentual", "valor_realizado_brl"], ascending=[True, False]
    ).head(10)

    return {
        "overview": overview,
        "category_summary": round_numeric_columns(category_summary),
        "group_summary": round_numeric_columns(group_summary),
        "top_distributors": round_numeric_columns(top_distributors),
        "attention_distributors": round_numeric_columns(attention_distributors),
    }


def round_numeric_columns(df):
    rounded = df.copy()
    for column in rounded.select_dtypes(include="number").columns:
        rounded[column] = rounded[column].round(2)
    return rounded


def save_kpi_summary(kpis):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sections = []

    for section_name in [
        "category_summary",
        "group_summary",
        "top_distributors",
        "attention_distributors",
    ]:
        section = kpis[section_name].copy()
        section.insert(0, "secao", section_name)
        sections.append(section)

    pd.concat(sections, ignore_index=True, sort=False).to_csv(
        KPI_SUMMARY_PATH, sep=";", decimal=",", index=False
    )


def format_number_br(value, decimals=2):
    return (
        f"{value:,.{decimals}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def format_integer_br(value):
    return f"{int(value):,}".replace(",", ".")


def format_currency_brl(value):
    return f"R$ {format_number_br(value)}"


def format_currency_usd(value):
    return f"US$ {format_number_br(value)}"


def format_percent(value):
    return f"{format_number_br(value)}%"


def format_markdown_table(df, columns):
    formatted = df.loc[:, columns].copy()

    for column in formatted.columns:
        if column.endswith("_brl"):
            formatted[column] = formatted[column].map(format_currency_brl)
        elif column.endswith("_usd"):
            formatted[column] = formatted[column].map(format_currency_usd)
        elif column.endswith("_percentual"):
            formatted[column] = formatted[column].map(format_percent)
        elif pd.api.types.is_numeric_dtype(formatted[column]):
            formatted[column] = formatted[column].map(format_number_br)

    headers = [str(column) for column in formatted.columns]
    rows = formatted.astype(str).values.tolist()

    header_line = "| " + " | ".join(headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    row_lines = ["| " + " | ".join(row) + " |" for row in rows]

    return "\n".join([header_line, separator_line, *row_lines])


def build_ai_prompt(kpis, quote_info):
    overview = kpis["overview"]
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote_warning = (
        "Atencao: a cotacao foi obtida por fallback local porque a API publica falhou."
        if quote_info["fallback"]
        else "A cotacao foi obtida por consulta em API publica."
    )

    category_table = format_markdown_table(
        kpis["category_summary"],
        [
            "categoria",
            "meta_unidades",
            "realizado_unidades",
            "atingimento_percentual",
            "valor_realizado_usd",
            "valor_realizado_brl",
            "cobertura_percentual",
            "premiacao_brl",
        ],
    )

    group_table = format_markdown_table(
        kpis["group_summary"],
        [
            "grupo_label",
            "meta_unidades",
            "realizado_unidades",
            "atingimento_percentual",
            "valor_realizado_brl",
            "cobertura_percentual",
            "premiacao_brl",
        ],
    )

    top_table = format_markdown_table(
        kpis["top_distributors"],
        [
            "distribuidor",
            "grupo_label",
            "realizado_unidades",
            "atingimento_percentual",
            "valor_realizado_brl",
            "cobertura_percentual",
            "premiacao_brl",
        ],
    )

    attention_table = format_markdown_table(
        kpis["attention_distributors"],
        [
            "distribuidor",
            "grupo_label",
            "realizado_unidades",
            "atingimento_percentual",
            "valor_realizado_brl",
            "cobertura_percentual",
            "premiacao_brl",
        ],
    )

    return f"""# Prompt para Analise Assistida por IA

Use o contexto e os dados abaixo para gerar uma analise comercial objetiva.

## Regras obrigatorias

- Nao invente numeros.
- Use apenas os dados fornecidos neste prompt.
- Se algum dado necessario nao estiver disponivel, informe a limitacao.
- Seja objetivo.
- Escreva em portugues.
- Foque em tomada de decisao comercial.
- Nao cite fontes externas.

## Saida esperada

Gere a resposta com as seguintes secoes:

1. Resumo executivo
2. Principais achados
3. Pontos de atencao
4. Recomendacoes praticas
5. Proximas analises sugeridas

## Contexto dos dados

Os dados representam uma campanha comercial ficticia de distribuidores. O KPI principal e volume em unidades. Os valores financeiros foram derivados por categoria usando uma regra de preco em dolar por unidade e convertidos para real com a cotacao USD/BRL abaixo.

- Prompt gerado em: {generated_at}
- Periodo analisado: {overview["periodo_inicio"]} a {overview["periodo_fim"]}
- Linhas analisadas: {format_integer_br(overview["linhas"])}
- Distribuidores: {format_integer_br(overview["distribuidores"])}
- Categorias: {format_integer_br(overview["categorias"])}
- Cotacao USD/BRL usada: R$ {format_number_br(quote_info["cotacao"], 4)}
- Fonte da cotacao: {quote_info["fonte"]}
- Observacao sobre cotacao: {quote_warning}

## Regra de valor por categoria

| categoria | unidades | valor_usd | valor_unitario_usd |
|---|---:|---:|---:|
{format_price_rules()}

## KPIs gerais

- Meta total em unidades: {format_number_br(overview["meta_unidades"])}
- Realizado total em unidades: {format_number_br(overview["realizado_unidades"])}
- Atingimento total: {format_percent(overview["atingimento_percentual"])}
- Diferenca total em unidades: {format_number_br(overview["diferenca_unidades"])}
- Valor meta em dolar: {format_currency_usd(overview["valor_meta_usd"])}
- Valor realizado em dolar: {format_currency_usd(overview["valor_realizado_usd"])}
- Valor meta em real: {format_currency_brl(overview["valor_meta_brl"])}
- Valor realizado em real: {format_currency_brl(overview["valor_realizado_brl"])}
- Diferenca de valor em real: {format_currency_brl(overview["diferenca_valor_brl"])}
- Cobertura media de meta: {format_percent(overview["cobertura_percentual"])}
- Premiacao total: {format_currency_brl(overview["premiacao_brl"])}

## Desempenho por categoria

{category_table}

## Desempenho por grupo

{group_table}

## Top 10 distribuidores por valor realizado em real

{top_table}

## 10 distribuidores com maior ponto de atencao por atingimento

{attention_table}

## Tarefa

Analise os dados fornecidos e gere uma leitura comercial para apoiar decisoes de gestao da campanha. Priorize implicacoes praticas sobre performance, cobertura, categorias, grupos e distribuidores. Nao extrapole para fora dos dados.
"""


def format_price_rules():
    rows = []
    for category, rule in CATEGORY_PRICE_RULES.items():
        unit_value = rule["usd_value"] / rule["units"]
        rows.append(
            "| "
            f"{category} | "
            f"{format_integer_br(rule['units'])} | "
            f"{format_currency_usd(rule['usd_value'])} | "
            f"{format_currency_usd(unit_value)} |"
        )
    return "\n".join(rows)


if __name__ == "__main__":
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_df = generate_dataset(save_csv=False)
    quote_info = get_usd_brl_quote()
    treated_df = prepare_dataset(raw_df, quote_info["cotacao"])
    kpis = build_kpis(treated_df)

    treated_df.to_csv(TREATED_DATASET_PATH, sep=";", decimal=",", index=False)
    save_kpi_summary(kpis)
    AI_PROMPT_PATH.write_text(build_ai_prompt(kpis, quote_info), encoding="utf-8")

    print("Pipeline concluida.")
    print(f"Dataset tratado: {TREATED_DATASET_PATH}")
    print(f"Resumo de KPIs: {KPI_SUMMARY_PATH}")
    print(f"Prompt para IA: {AI_PROMPT_PATH}")
    print(quote_info["mensagem"])
