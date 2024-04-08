import pandas as pd

from pandas import DataFrame

from pathlib import Path
# Caminho para o arquivo Excel
caminho_arquivo: Path = Path("data/inventario_mundo.xlsx")

# Lendo o arquivo
df: DataFrame = pd.read_excel(caminho_arquivo)

# Exibindo as primeiras linhas do DataFrame
print(df.head())
df_estoque_baixo: DataFrame = df[df["quantidade_estoque"] > 10]
print(df_estoque_baixo)

disponiveis_e_baixo_estoque = df[(df["disponivel_venda"] == True) & (df["quantidade_estoque"] < 10)]
print(disponiveis_e_baixo_estoque)

df["valor_total_estoque"] = df["quantidade_estoque"] * df["preco_unitario"]
valor_total = df["valor_total_estoque"].sum()
print("Valor total em estoque:", valor_total)

ordenado_por_preco = df.sort_values(by="preco_unitario", ascending=False)
print(ordenado_por_preco)

contagem_por_disponibilidade = df["disponivel_venda"].value_counts()
print(contagem_por_disponibilidade)
