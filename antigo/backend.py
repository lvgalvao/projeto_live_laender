import pandera as pa
from pandera import DataFrameSchema
from pandera.typing import DateTime, String, Int, Float, Bool, Series

class InventarioSchema(pa.DataFrameModel):
    nome_produto: String = pa.Field()
    quantidade_estoque: Int = pa.Field()
    preco_unitario: Float = pa.Field()
    disponivel_venda: Bool = pa.Field()
    data_validade: DateTime = pa.Field()

    class Config:
        strict = True

schema = InventarioSchema.to_schema()

import pandas as pd

# Carregar o DataFrame do arquivo Excel
df = pd.read_excel("inventario_mundo_v3.xlsx")

# Validar o DataFrame
try:
    new_df = schema.validate(df, lazy=True)
    print(new_df)
    print("Validação do esquema bem-sucedida!")
except:
    print(f"Erro de validação")
