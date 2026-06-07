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

- Prompt gerado em: 2026-06-07 14:11:51
- Periodo analisado: 2025-01-01 a 2025-12-31
- Linhas analisadas: 173.740
- Distribuidores: 68
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

- Meta total em unidades: 95.449.378,00
- Realizado total em unidades: 92.299.680,82
- Atingimento total: 96,70%
- Diferenca total em unidades: -3.149.697,18
- Valor meta em dolar: US$ 449.797.794,50
- Valor realizado em dolar: US$ 435.250.629,89
- Valor meta em real: R$ 2.324.150.175,95
- Valor realizado em real: R$ 2.248.983.526,60
- Diferenca de valor em real: R$ -75.166.649,35
- Cobertura media de meta: 46,45%
- Premiacao total: R$ 80.701.000,00

## Desempenho por categoria

| categoria | meta_unidades | realizado_unidades | atingimento_percentual | valor_realizado_usd | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAFÉ | 13.563.251,00 | 13.162.482,67 | 97,05% | US$ 105.299.861,36 | R$ 544.094.912,94 | 46,60% | R$ 11.567.000,00 |
| CHOCOLATE | 13.671.932,00 | 13.243.364,21 | 96,87% | US$ 92.703.549,47 | R$ 479.008.511,04 | 46,54% | R$ 11.551.000,00 |
| CEREAL | 13.697.226,00 | 13.230.047,72 | 96,59% | US$ 66.150.238,60 | R$ 341.804.898,33 | 46,20% | R$ 11.468.000,00 |
| LEITE | 13.577.057,00 | 13.124.814,51 | 96,67% | US$ 52.499.258,04 | R$ 271.268.916,43 | 46,54% | R$ 11.550.000,00 |
| CREME DE LEITE | 13.632.080,00 | 13.184.783,14 | 96,72% | US$ 46.146.740,59 | R$ 238.444.824,80 | 46,61% | R$ 11.569.000,00 |
| OUTROS | 13.624.089,00 | 13.131.018,73 | 96,38% | US$ 39.393.056,19 | R$ 203.547.861,08 | 46,41% | R$ 11.518.000,00 |
| AÇÚCAR | 13.683.743,00 | 13.223.169,84 | 96,63% | US$ 33.057.925,64 | R$ 170.813.601,98 | 46,24% | R$ 11.478.000,00 |

## Desempenho por grupo

| grupo_label | meta_unidades | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Grupo 1 | 26.595.759,00 | 26.889.519,44 | 101,10% | R$ 655.160.775,89 | 54,07% | R$ 26.247.000,00 |
| Grupo 4 | 21.063.449,00 | 20.653.635,29 | 98,05% | R$ 503.392.860,33 | 46,71% | R$ 17.901.000,00 |
| Grupo 2 | 16.892.018,00 | 15.368.449,51 | 90,98% | R$ 374.378.880,93 | 38,13% | R$ 11.690.000,00 |
| Grupo 5 | 15.488.477,00 | 15.182.617,20 | 98,03% | R$ 370.066.160,22 | 51,39% | R$ 14.442.000,00 |
| Grupo 3 | 15.409.675,00 | 14.205.459,38 | 92,19% | R$ 345.984.849,23 | 37,08% | R$ 10.421.000,00 |

## Top 10 distribuidores por valor realizado em real

| distribuidor | grupo_label | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Atacadão Fort | Grupo 1 | 2.333.338,66 | 167,49% | R$ 56.880.484,75 | 99,96% | R$ 2.554.000,00 |
| Loja Alabama | Grupo 4 | 2.277.004,60 | 162,93% | R$ 55.819.335,13 | 99,88% | R$ 2.552.000,00 |
| Distribuidora Nova Era | Grupo 2 | 2.184.839,20 | 157,90% | R$ 53.063.240,88 | 99,88% | R$ 2.552.000,00 |
| Atacadão Prime | Grupo 5 | 1.984.701,13 | 138,84% | R$ 48.288.882,83 | 97,61% | R$ 2.494.000,00 |
| Armazém Aliança | Grupo 2 | 1.921.906,83 | 134,75% | R$ 47.052.749,04 | 95,97% | R$ 2.452.000,00 |
| Distribuidora São José | Grupo 1 | 1.918.614,09 | 135,24% | R$ 46.846.422,37 | 96,44% | R$ 2.464.000,00 |
| Distribuidora Fort | Grupo 1 | 1.916.825,09 | 137,32% | R$ 46.796.139,53 | 97,03% | R$ 2.479.000,00 |
| Atacadão Aliança | Grupo 1 | 1.915.179,81 | 139,19% | R$ 46.610.908,06 | 97,61% | R$ 2.494.000,00 |
| Supermercado Prime | Grupo 4 | 1.889.829,52 | 136,40% | R$ 46.315.730,35 | 96,44% | R$ 2.464.000,00 |
| Loja Brasil | Grupo 1 | 1.882.247,34 | 134,86% | R$ 45.928.137,03 | 96,28% | R$ 2.460.000,00 |

## 10 distribuidores com maior ponto de atencao por atingimento

| distribuidor | grupo_label | realizado_unidades | atingimento_percentual | valor_realizado_brl | cobertura_percentual | premiacao_brl |
| --- | --- | --- | --- | --- | --- | --- |
| Loja Prime | Grupo 2 | 263.351,06 | 18,91% | R$ 6.397.536,39 | 0,00% | R$ 0,00 |
| Mercado Nova Era | Grupo 1 | 433.948,12 | 31,32% | R$ 10.569.690,34 | 0,04% | R$ 1.000,00 |
| Atacadão Express | Grupo 5 | 447.111,67 | 31,77% | R$ 10.966.393,43 | 0,00% | R$ 0,00 |
| Empório Nova Era | Grupo 1 | 483.606,94 | 34,58% | R$ 11.836.184,75 | 0,00% | R$ 0,00 |
| Empório São José | Grupo 1 | 669.308,99 | 48,15% | R$ 16.369.195,32 | 0,47% | R$ 12.000,00 |
| Atacadão Nova Era | Grupo 4 | 747.158,58 | 53,52% | R$ 18.218.911,85 | 0,74% | R$ 19.000,00 |
| Armazém Fort | Grupo 4 | 826.175,47 | 57,99% | R$ 20.156.118,72 | 1,41% | R$ 36.000,00 |
| Armazém Alabama | Grupo 4 | 867.471,38 | 61,71% | R$ 21.054.496,97 | 3,33% | R$ 85.000,00 |
| Atacadão Central | Grupo 2 | 878.868,03 | 62,07% | R$ 21.408.702,26 | 2,54% | R$ 65.000,00 |
| Distribuidora Alabama | Grupo 3 | 932.120,92 | 66,23% | R$ 22.569.236,04 | 4,23% | R$ 108.000,00 |

## Tarefa

Analise os dados fornecidos e gere uma leitura comercial para apoiar decisoes de gestao da campanha. Priorize implicacoes praticas sobre performance, cobertura, categorias, grupos e distribuidores. Nao extrapole para fora dos dados.
