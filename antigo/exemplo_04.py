import pandera as pa
from pandera.typing import DateTime, String, Int, Float, Bool

class InventarioSchema(pa.DataFrameModel):
    nome_produto: String = pa.Field(unique=True)
    quantidade_estoque: Int = pa.Field(nullable=False)
    preco_unitario: Float = pa.Field(ge=0)
    disponivel_venda: Bool = pa.Field(nullable=True)
    data_validade: DateTime = pa.Field()

    class Config:
        strict = True  # Garante que apenas as colunas definidas estão presentes
        coerce=True

import pandas as pd

# Carregar o DataFrame do arquivo Excel
df = pd.read_excel("inventario_mundo_preco_com_virgula_e_ponto.xlsx")

# Validar o DataFrame
try:
    InventarioSchema.validate(df)
    print(df)
    print("Validação do esquema bem-sucedida!")
except pa.errors.SchemaError as e:
    print(f"Erro de validação: {e}")