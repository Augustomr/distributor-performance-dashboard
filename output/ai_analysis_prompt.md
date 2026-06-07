# Prompt para Analise Assistida por IA

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

- Prompt gerado em: 2026-06-07 13:57:38
- Periodo analisado: 2025-01-01 a 2025-12-31
- Linhas analisadas: 168.630
- Distribuidores: 66
- Categorias: 7
- Cotacao USD/BRL usada: R$ 5,1671
- Fonte da cotacao: https://economia.awesomeapi.com.br/json/last/USD-BRL
- Observacao sobre cotacao: A cotacao foi obtida por consulta em API publica.

## Regra de valor por categoria

| categoria | unidades | valor_usd | valor_unitario_usd |
|---|---:|---:|---:|
| CEREAL | 10 | US$ 50,00 | US$ 5,00 |
| CREME DE LEITE | 10 | US$ 35,00 | US$ 3,50 |
| AÇÚCAR | 10 | US$ 25,00 | US$ 2,50 |
| LEITE | 10 | US$ 40,00 | US$ 4,00 |
| CAFÉ | 10 | US$ 80,00 | US$ 8,00 |
| CHOCOLATE | 10 | US$ 70,00 | US$ 7,00 |
| OUTROS | 10 | US$ 30,00 | US$ 3,00 |

## KPIs gerais

- Meta total em unidades: 92.656.244,00
- Realizado total em unidades: 92.895.157,10
- Atingimento total: 100,26%
- Diferenca total em unidades: 238.913,10
- Valor meta em dolar: US$ 436.688.223,50
- Valor realizado em dolar: US$ 437.803.686,25
- Valor meta em real: R$ 2.256.411.712,30
- Valor realizado em real: R$ 2.262.175.423,72
- Diferenca de valor em real: R$ 5.763.711,42
- Cobertura media de meta: 48,54%
- Premiacao total: R$ 81.858.000,00

## Desempenho por categoria

| categoria | meta_unidades | realizado_unidades | atingimento_percentual | valor_realizado_usd | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAFÉ | 13.213.870,00 | 13.232.098,49 | 100,14% | US$ 105.856.787,92 | R$ 546.972.608,67 | 48,48% | R$ 11.679.000,00 |
| CHOCOLATE | 13.239.168,00 | 13.284.002,82 | 100,34% | US$ 92.988.019,74 | R$ 480.478.396,77 | 48,65% | R$ 11.719.000,00 |
| CEREAL | 13.242.798,00 | 13.284.846,91 | 100,32% | US$ 66.424.234,55 | R$ 343.220.662,87 | 48,48% | R$ 11.679.000,00 |
| LEITE | 13.194.915,00 | 13.233.505,82 | 100,29% | US$ 52.934.023,28 | R$ 273.515.391,51 | 48,54% | R$ 11.693.000,00 |
| CREME DE LEITE | 13.277.346,00 | 13.305.297,97 | 100,21% | US$ 46.568.542,70 | R$ 240.624.318,67 | 48,73% | R$ 11.738.000,00 |
| OUTROS | 13.236.718,00 | 13.287.128,69 | 100,38% | US$ 39.861.386,07 | R$ 205.967.768,02 | 48,46% | R$ 11.674.000,00 |
| AÇÚCAR | 13.251.429,00 | 13.268.276,40 | 100,13% | US$ 33.170.691,99 | R$ 171.396.277,21 | 48,47% | R$ 11.676.000,00 |

## Desempenho por grupo

| grupo_label | meta_unidades | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo 2 | 28.095.185,00 | 29.643.295,23 | 105,51% | R$ 722.563.519,40 | 53,95% | R$ 27.571.000,00 |
| Grupo 4 | 22.397.324,00 | 21.570.641,73 | 96,31% | R$ 524.513.244,12 | 44,18% | R$ 18.061.000,00 |
| Grupo 5 | 14.098.898,00 | 14.219.811,64 | 100,86% | R$ 345.825.468,12 | 51,87% | R$ 13.254.000,00 |
| Grupo 3 | 15.460.378,00 | 13.942.455,79 | 90,18% | R$ 339.535.571,72 | 39,40% | R$ 11.073.000,00 |
| Grupo 1 | 12.604.459,00 | 13.518.952,71 | 107,26% | R$ 329.737.620,36 | 51,75% | R$ 11.899.000,00 |

## Top 10 distribuidores por valor realizado em real

| distribuidor | grupo_label | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Loja Fort | Grupo 1 | 2.490.946,03 | 175,77% | R$ 60.768.999,41 | 100,00% | R$ 2.555.000,00 |
| Empório Express | Grupo 2 | 2.346.284,02 | 165,93% | R$ 57.004.467,41 | 99,96% | R$ 2.554.000,00 |
| Armazém Aliança | Grupo 3 | 2.248.695,21 | 161,10% | R$ 54.567.035,17 | 99,88% | R$ 2.552.000,00 |
| Mercado Fort | Grupo 2 | 2.220.948,58 | 156,58% | R$ 54.080.005,10 | 99,84% | R$ 2.551.000,00 |
| Loja Aliança | Grupo 2 | 2.076.727,68 | 148,08% | R$ 50.747.611,68 | 99,26% | R$ 2.536.000,00 |
| Loja Prime | Grupo 1 | 2.052.917,54 | 146,34% | R$ 50.122.729,49 | 98,94% | R$ 2.528.000,00 |
| Distribuidora Alabama | Grupo 4 | 2.001.291,60 | 142,18% | R$ 48.868.158,76 | 98,24% | R$ 2.510.000,00 |
| Armazém Alabama | Grupo 4 | 1.995.804,67 | 143,38% | R$ 48.633.126,93 | 98,79% | R$ 2.524.000,00 |
| Mercado Prime | Grupo 1 | 1.903.296,33 | 133,76% | R$ 46.564.733,93 | 95,97% | R$ 2.452.000,00 |
| Empório São José | Grupo 4 | 1.892.132,00 | 135,70% | R$ 45.976.608,87 | 96,32% | R$ 2.461.000,00 |

## 10 distribuidores com maior ponto de atencao por atingimento

| distribuidor | grupo_label | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Armazém Prime | Grupo 3 | 519.717,22 | 37,07% | R$ 12.493.176,94 | 0,20% | R$ 5.000,00 |
| Atacadão Nova Era | Grupo 3 | 731.541,04 | 52,18% | R$ 17.801.816,83 | 0,98% | R$ 25.000,00 |
| Loja Alabama | Grupo 4 | 751.359,17 | 53,30% | R$ 18.347.673,19 | 0,82% | R$ 21.000,00 |
| Mercado Central | Grupo 1 | 788.284,41 | 56,05% | R$ 19.348.801,00 | 1,49% | R$ 38.000,00 |
| Supermercado Prime | Grupo 4 | 880.794,94 | 63,27% | R$ 21.451.570,49 | 3,56% | R$ 91.000,00 |
| Empório Alabama | Grupo 3 | 919.223,71 | 64,44% | R$ 22.433.807,24 | 3,25% | R$ 83.000,00 |
| Comercial Express | Grupo 4 | 900.057,36 | 65,09% | R$ 21.893.881,01 | 3,48% | R$ 89.000,00 |
| Empório Central | Grupo 2 | 916.505,89 | 65,36% | R$ 22.355.066,65 | 4,54% | R$ 116.000,00 |
| Armazém Express | Grupo 2 | 911.024,57 | 65,63% | R$ 22.318.211,23 | 4,23% | R$ 108.000,00 |
| Supermercado Nova Era | Grupo 2 | 919.279,43 | 66,23% | R$ 22.462.579,49 | 5,24% | R$ 134.000,00 |

## Tarefa

Analise os dados fornecidos e gere uma leitura comercial para apoiar decisoes de gestao da campanha. Priorize implicacoes praticas sobre performance, cobertura, categorias, grupos e distribuidores. Nao extrapole para fora dos dados.
