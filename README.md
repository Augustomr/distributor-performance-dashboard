# Distributor Performance Dashboard

Projeto de portfólio voltado para análise de desempenho de distribuidores em uma campanha de incentivo comercial.

O repositório reúne geração de dados sintéticos em Python, tratamento em pipeline, enriquecimento financeiro com cotação de dólar, geração de KPIs, dashboard em Power BI, relatório em PDF e um prompt Markdown pronto para análise assistida por IA.

## Objetivo

Simular um cenário de negócio em que uma empresa precisa acompanhar:

- quais distribuidores estão atingindo meta;
- como a performance varia entre categorias;
- como a premiação está sendo distribuída;
- onde existem gaps de cobertura e oportunidade de crescimento;
- qual é o impacto financeiro do volume realizado em dólar e em real;
- como transformar KPIs calculados em uma análise executiva com apoio de IA, sem usar API paga.

Os dados são fictícios, mas foram estruturados para parecerem próximos de um contexto real de acompanhamento comercial.

## Estrutura do projeto

```text
distributor-performance-dashboard/
|-- dashboard/
|   `-- Analysis_Dashboard.pbix
|-- data/
|   |-- dataset.csv
|   `-- dataset_tratado.csv
|-- output/
|   |-- ai_analysis_prompt.md
|   `-- kpis_resumo.csv
|-- report/
|   `-- resultado_campanha.pdf
|-- scripts/
|   |-- generate_data.py
|   `-- pipeline.py
`-- README.md
```

## Arquivos principais

- `scripts/generate_data.py`: gera a base sintética usada no projeto.
- `scripts/pipeline.py`: executa a pipeline local de tratamento, valorização financeira, KPIs e prompt para IA.
- `data/dataset.csv`: dataset original exportado pelo gerador.
- `data/dataset_tratado.csv`: dataset tratado pela pipeline, com campos amigáveis e colunas financeiras.
- `output/kpis_resumo.csv`: resumo consolidado de KPIs por categoria, grupo e distribuidor.
- `output/ai_analysis_prompt.md`: prompt pronto para colar no ChatGPT/Codex e obter uma análise comercial.
- `dashboard/Analysis_Dashboard.pbix`: dashboard analítico em Power BI.
- `report/resultado_campanha.pdf`: relatório final com leitura dos resultados da campanha.

## Dataset original

O arquivo `data/dataset.csv` está salvo com `;` como separador e `,` como decimal, padrão comum em ambientes PT-BR.

Campos originais:

- `Distributor_ID`: identificador do distribuidor
- `Distributor`: nome sintético do distribuidor
- `Grupo`: grupo do distribuidor
- `Categoria`: categoria de produto
- `kpiType`: tipo do KPI analisado
- `isFocusCategory`: indicador de categoria foco
- `Meta`: meta definida para o período
- `Realizado`: resultado realizado em volume/unidades
- `Data`: data de referência
- `Premiacao`: valor de premiação concedido
- `Cobertura`: flag de atingimento de meta
- `Distributor_Num`: identificador numérico auxiliar
- `Grupo_Label`: rótulo textual do grupo

## Pipeline Python

A pipeline foi criada para tratar os dados antes da análise, sem usar OpenAI API ou qualquer serviço pago de IA.

Ela executa as seguintes etapas:

1. Obtém os dados sintéticos chamando `generate_dataset(save_csv=False)`, sem gerar arquivo intermediário.
2. Renomeia colunas para nomes mais amigáveis.
3. Aplica uma regra de preço por categoria, considerando que o KPI original é volume/unidades.
4. Consulta uma API pública para obter a cotação USD/BRL.
5. Calcula valores realizados em dólar e em real.
6. Calcula KPIs comerciais.
7. Gera um prompt Markdown para análise assistida por IA.

### Regra de valor por categoria

O campo `Realizado` representa volume, não dinheiro. Por isso, a pipeline usa uma regra comercial por categoria.

Exemplo:

```text
10 unidades CEREAL = US$ 50,00
1 unidade CEREAL = US$ 5,00

valor_realizado_usd = realizado_unidades * valor_unitario_usd
valor_realizado_brl = valor_realizado_usd * cotacao_dolar_brl
```

As regras ficam definidas em `CATEGORY_PRICE_RULES`, dentro de `scripts/pipeline.py`.

### Colunas geradas no dataset tratado

Além dos campos renomeados, o arquivo `data/dataset_tratado.csv` inclui:

- `unidades_regra_preco`
- `valor_regra_usd`
- `valor_unitario_usd`
- `cotacao_dolar_brl`
- `valor_meta_usd`
- `valor_realizado_usd`
- `valor_meta_brl`
- `valor_realizado_brl`
- `diferenca_unidades`
- `diferenca_valor_brl`
- `atingimento_percentual`

## Prompt para análise assistida por IA

O arquivo `output/ai_analysis_prompt.md` é gerado automaticamente pela pipeline.

Ele contém:

- contexto dos dados;
- regras obrigatórias para a IA;
- resumo dos KPIs gerais;
- desempenho por categoria;
- desempenho por grupo;
- top distribuidores;
- distribuidores com maior ponto de atenção;
- instruções para gerar uma análise comercial em português.

O prompt orienta a IA a gerar:

- resumo executivo;
- principais achados;
- pontos de atenção;
- recomendações práticas;
- próximas análises sugeridas.

Também deixa explícito que a IA deve:

- não inventar números;
- usar apenas os dados fornecidos;
- ser objetiva;
- escrever em português;
- focar em tomada de decisão comercial.

## Como executar

### Pré-requisitos

- Python 3.10+ recomendado
- dependências instaladas no ambiente:

```bash
pip install pandas numpy
```

### Gerar apenas o dataset original

```bash
python scripts/generate_data.py
```

Ao executar, o arquivo `data/dataset.csv` é sobrescrito com uma nova amostra sintética.

### Executar a pipeline completa

```bash
python scripts/pipeline.py
```

Ao executar, são gerados:

- `data/dataset_tratado.csv`
- `output/kpis_resumo.csv`
- `output/ai_analysis_prompt.md`

A pipeline consulta a cotação USD/BRL na API pública da AwesomeAPI. Caso a consulta falhe, usa um valor local de fallback e registra essa informação no prompt gerado.

## Dashboard

O arquivo `dashboard/Analysis_Dashboard.pbix` foi construído para apoiar leituras como:

- visão geral de performance;
- atingimento de meta por distribuidor;
- comparação por categoria;
- análise de cobertura;
- distribuição de premiação.

## Relatório

O arquivo `report/resultado_campanha.pdf` complementa o dashboard com uma narrativa executiva dos resultados observados na campanha.

## Tecnologias utilizadas

- Python
- pandas
- numpy
- Power BI
- Markdown
- API pública de cotação USD/BRL

## Observações

- Todos os dados do projeto são fictícios.
- A solução de análise assistida por IA é local no projeto e não usa OpenAI API.
- O prompt gerado deve ser colado manualmente no ChatGPT/Codex ou em outra IA de preferência.
- Caso os scripts sejam executados novamente, os dados sintéticos e os KPIs podem mudar.

## Autor

Augusto Rocha  
Data Analyst | Data Engineering
