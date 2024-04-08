from pathlib import Path

import pandas as pd
from pandas import DataFrame

from contrato_de_dados import InventarioDoMundoSchema

# Caminho para o arquivo Excel
caminho_arquivo: Path = Path("data/inventario_mundo_sem_coluna.xlsx")

# Lendo o arquivo
df: DataFrame = pd.read_excel(caminho_arquivo)

# Validar o DataFrame
try:
    new_df = InventarioDoMundoSchema.validate(df)
    print(new_df)
    print("Validação do esquema bem-sucedida!")
except InventarioDoMundoSchema as e:
    print(f"Erro de validação: {e}")