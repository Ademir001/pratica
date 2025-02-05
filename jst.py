import pandas as pd 
import json 
with open("clientes.json", "r") as arq:
    dados = json.load(arq)
clientes = []
for cliente in dados:
    for vi in cliente["Dados"]:
        clientes.append({
            "cliente_id": cliente["cliente_id"],
            "data_acesso": cliente["data_acesso"],
            "tipo": vi["tipo"],
            "detalhes": vi.get("termo") or vi.get("produto_id") or vi.get("valor")

    })
df = pd.DataFrame(clientes)
print(df.head())