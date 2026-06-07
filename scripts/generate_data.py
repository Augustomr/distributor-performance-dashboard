from pathlib import Path
import random

import numpy as np
import pandas as pd


NUM_DISTRIBUTORS_MIN = 50
NUM_DISTRIBUTORS_MAX = 100
START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

CATEGORIES = [
    "CEREAL",
    "CREME DE LEITE",
    "AÇÚCAR",
    "LEITE",
    "CAFÉ",
    "CHOCOLATE",
    "OUTROS",
]

KPI_TYPES = ["TOTAL_VOLUME"]

NAME_PREFIX = [
    "Mercado",
    "Loja",
    "Supermercado",
    "Atacadão",
    "Distribuidora",
    "Comercial",
    "Empório",
    "Armazém",
]

NAME_SUFFIX = [
    "Central",
    "Aliança",
    "São José",
    "Prime",
    "Brasil",
    "Fort",
    "Express",
    "Alabama",
    "Nova Era",
]

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET_PATH = PROJECT_ROOT / "data" / "dataset.csv"


def generate_distributors(n):
    available_names = [
        f"{prefix} {suffix}" for prefix in NAME_PREFIX for suffix in NAME_SUFFIX
    ]

    if n > len(available_names):
        raise ValueError(
            f"Nao e possivel gerar {n} distribuidores unicos. "
            f"O maximo atual e {len(available_names)}."
        )

    return random.sample(available_names, n)


def generate_dataset(save_csv=False, output_path=DEFAULT_DATASET_PATH):
    max_available_distributors = len(NAME_PREFIX) * len(NAME_SUFFIX)
    num_distributors = random.randint(
        NUM_DISTRIBUTORS_MIN,
        min(NUM_DISTRIBUTORS_MAX, max_available_distributors),
    )
    distributors = generate_distributors(num_distributors)
    dates = pd.date_range(start=START_DATE, end=END_DATE, freq="D")

    data = []

    for dist_id, distributor in enumerate(distributors, start=1):
        grupo = random.randint(1, 5)
        performance_factor = np.random.normal(1, 0.3)

        for date in dates:
            for category in CATEGORIES:
                meta = random.randint(100, 1000)
                variation = np.random.normal(performance_factor, 0.2)
                realizado = max(0, meta * variation)
                premiacao = 1000 if realizado >= meta else 0
                cobertura = 1 if realizado >= meta else 0

                data.append(
                    {
                        "Distributor_ID": dist_id,
                        "Distributor": distributor,
                        "Grupo": grupo,
                        "Categoria": category,
                        "kpiType": "TOTAL_VOLUME",
                        "isFocusCategory": random.choice([0, 1]),
                        "Meta": round(meta, 2),
                        "Realizado": round(realizado, 2),
                        "Data": date.strftime("%Y-%m-%d"),
                        "Premiacao": premiacao,
                        "Cobertura": cobertura,
                        "Distributor_Num": dist_id,
                        "Grupo_Label": f"Grupo {grupo}",
                    }
                )

    df = pd.DataFrame(data)

    if save_csv:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, sep=";", decimal=",", index=False)

    return df


def main():
    df = generate_dataset(save_csv=True)
    print(
        "Dataset gerado com "
        f"{len(df)} linhas, "
        f"{df['Distributor_ID'].nunique()} distribuidores, "
        f"{df['Categoria'].nunique()} categorias e "
        f"{df['Data'].nunique()} datas."
    )


if __name__ == "__main__":
    main()
