# Distributor Performance Dashboard

Projeto de portfólio voltado para análise de desempenho de distribuidores em uma campanha de incentivo comercial. O repositório reúne um gerador de dados sintéticos em Python, um dataset pronto para uso, um dashboard em Power BI e um relatório em PDF com a leitura dos resultados.

## Objetivo

Simular um cenário de negócio em que uma empresa precisa acompanhar:

- quais distribuidores estão atingindo meta;
- como a performance varia entre categorias;
- como a premiação está sendo distribuída;
- onde existem gaps de cobertura e oportunidade de crescimento.

Os dados são fictícios, mas foram estruturados para parecerem próximos de um contexto real de acompanhamento comercial.

## Estrutura do projeto

```text
distributor-performance-dashboard/
|-- dashboard/
|   `-- Analysis_Dashboard.pbix
|-- data/
|   `-- dataset.csv
|-- report/
|   `-- resultado_campanha.pdf
|-- scripts/
|   `-- generate_data.py
`-- README.md
```

## Arquivos principais

- `scripts/generate_data.py`: gera a base sintética usada no projeto.
- `data/dataset.csv`: dataset consolidado já exportado.
- `dashboard/Analysis_Dashboard.pbix`: dashboard analítico em Power BI.
- `report/resultado_campanha.pdf`: relatório final com os principais resultados da campanha.

## Dataset

O arquivo `data/dataset.csv` está salvo com `;` como separador e `,` como decimal, padrão comum em ambientes PT-BR.

Base atual do repositório:

- 145.635 linhas
- 13 colunas
- 57 distribuidores únicos
- 7 categorias
- período de `2025-01-01` a `2025-12-31`

### Campos disponíveis

- `Distributor_ID`: identificador do distribuidor
- `Distributor`: nome sintético do distribuidor
- `Grupo`: grupo do distribuidor
- `Categoria`: categoria de produto
- `kpiType`: tipo do KPI analisado
- `isFocusCategory`: indicador de categoria foco
- `Meta`: meta definida para o período
- `Realizado`: resultado realizado
- `Data`: data de referência
- `Premiacao`: valor de premiação concedido
- `Cobertura`: flag de atingimento de meta
- `Distributor_Num`: identificador numérico auxiliar
- `Grupo_Label`: rótulo textual do grupo

## Como gerar os dados

O script atual usa `pandas`, `numpy`, `random` e `datetime`.

### Pré-requisitos

- Python 3.10+ recomendado
- dependências instaladas no ambiente:

```bash
pip install pandas numpy
```

### Execução

```bash
python scripts/generate_data.py
```

Ao executar, o arquivo `data/dataset.csv` é sobrescrito com uma nova amostra sintética.

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

## Observações

- Todos os dados do projeto são fictícios.
- O repositório foi desenvolvido com foco em portfólio de análise de dados.
- Caso o script seja alterado, o conteúdo do dataset pode mudar em volume e distribuição.

## Autor

Augusto Rocha  
Data Analyst | Data Engineering
