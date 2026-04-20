import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -----------------------
# CONFIG INICIAL -> Informações básicas para geração do dataset
# -----------------------
NUM_DISTRIBUTORS = random.randint(50, 100)
START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

CATEGORIES = [
    "CEREAL", "CREME DE LEITE", "AÇÚCAR",
    "LEITE", "CAFÉ", "CHOCOLATE", "OUTROS"
]

KPI_TYPES = ["TOTAL_VOLUME"]

NAME_PREFIX = [
    "Mercado", "Loja", "Supermercado", "Atacadão",
    "Distribuidora", "Comercial", "Empório", "Armazém"
]

NAME_SUFFIX = [
    "Central", "Aliança", "São José", "Prime",
    "Brasil", "Fort", "Express", "Alabama", "Nova Era"
]

# -----------------------
# GERAR DISTRIBUIDORES -> Gerar nomes únicos de distribuidores combinando prefixos e sufixos
# -----------------------
def generate_distributors(n):
    names = set()
    while len(names) < n:
        name = f"{random.choice(NAME_PREFIX)} {random.choice(NAME_SUFFIX)}"
        names.add(name)
    return list(names)

distributors = generate_distributors(NUM_DISTRIBUTORS)

# -----------------------
# GERAR DATAS -> Gerar uma lista de datas diárias entre a data de início e fim
# -----------------------
dates = pd.date_range(start=START_DATE, end=END_DATE, freq='D')

# -----------------------
# GERAR DADOS
# -----------------------
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

            data.append({
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
                "Grupo_Label": f"Grupo {grupo}"
            })

df = pd.DataFrame(data)

# -----------------------
# SALVAR -> Salvar o dataset gerado em um arquivo CSV
# -----------------------
df.to_csv("data/dataset.csv", index=False)

print(f"Dataset gerado com {len(df)} linhas, {NUM_DISTRIBUTORS} distribuidores, {len(CATEGORIES)} categorias e {len(dates)} datas.")
