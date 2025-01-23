import pandas as pd 
import json

with open("clientes.json", "r") as arq:
    dados = json.load(arq)
clientes = []
for cliente in dados:
    for acao in cliente["acoes"]:
        clientes.append({
            "cliente_id": cliente["cliente_id"],
            "data_acesso": cliente["data_acesso"],
            "tipo": acao["tipo"],
            "detalhes": acao.get("termo") or acao.get("produto_id") or acao.get("valor")
        })

# Converter para DataFrame para análise
df = pd.DataFrame(clientes)
print(df.head())