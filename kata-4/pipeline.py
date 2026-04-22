import unicodedata
import pandas as pd
import os

base_path = os.path.dirname(__file__)

def normalizar_cidade(c):
    c = str(c).strip().lower()
    return ''.join(
        ch for ch in unicodedata.normalize('NFD', c)
        if unicodedata.category(ch) != 'Mn'
    )

pedidos = pd.read_csv(os.path.join(base_path, "pedidos.csv"), sep=";")
clientes = pd.read_csv(os.path.join(base_path, "clientes.csv"), sep=";")
entregas = pd.read_csv(os.path.join(base_path, "entregas.csv"), sep=";")

pedidos["valor_total"] = pedidos["valor_total"].astype(str).str.replace(",", ".").astype(float)
clientes["cidade"] = clientes["cidade"].apply(normalizar_cidade)

df = pedidos.merge(clientes, on="id_cliente", how="left")
df = df.merge(entregas, on="id_pedido", how="left")

df["atraso_dias"] = (
    pd.to_datetime(df["data_realizada"], errors="coerce") -
    pd.to_datetime(df["data_prevista"], errors="coerce")
).dt.days

df.to_csv(os.path.join(base_path, "consolidado.csv"), index=False, sep=";")

print("Pipeline executado")

print("\n--- INDICADORES ---")

# Total de pedidos por status
print("\nTotal por status:")
print(df["status"].value_counts())

# Ticket médio por estado
print("\nTicket médio por estado:")
print(df.groupby("estado")["valor_total"].mean())

# Percentual de entregas no prazo vs atraso
entregues = df[df["data_realizada"].notna()]
no_prazo = (entregues["atraso_dias"] <= 0).sum()
atraso = (entregues["atraso_dias"] > 0).sum()

total_entregues = len(entregues)

if total_entregues > 0:
    print("\nEntregas no prazo (%):", (no_prazo / total_entregues) * 100)
    print("Entregas com atraso (%):", (atraso / total_entregues) * 100)

# Top 3 cidades com mais pedidos
print("\nTop 3 cidades:")
print(df["cidade"].value_counts().head(3))

# Média de atraso (só pedidos atrasados)
atrasados = df[df["atraso_dias"] > 0]

if len(atrasados) > 0:
    print("\nMédia de atraso (dias):")
    print(atrasados["atraso_dias"].mean())