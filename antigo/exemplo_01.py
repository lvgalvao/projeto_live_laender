import pandera as pa
from pandera.typing import DateTime, String, Int, Float, Bool

class InventarioSchema(pa.DataFrameModel):
    nome_produto: String = pa.Field(unique=True)
    quantidade_estoque: Int = pa.Field()
    preco_unitario: Float = pa.Field()
    disponivel_venda: Bool = pa.Field()
    data_validade: DateTime = pa.Field()

    class Config:
        strict = True  # Garante que apenas as colunas definidas estão presentes

schema = InventarioSchema.to_schema()

import pandas as pd

# Carregar o DataFrame do arquivo Excel
df = pd.read_excel("inventario_mundo_erro_nao_unico.xlsx")

# Validar o DataFrame
try:
    new_df = schema.validate(df)
    print(new_df)
    print("Validação do esquema bem-sucedida!")
except pa.errors.SchemaError as e:
    print(f"Erro de validação: {e}")