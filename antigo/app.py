import streamlit as st
import pandas as pd
import pandera as pa
from pandera.typing import String, Int, Float, Bool, DateTime

class InventarioSchema(pa.DataFrameModel):
    nome_produto: String = pa.Field(nullable=True, unique=True)
    quantidade_estoque: Int = pa.Field(ge=0, le=30)
    preco_unitario: Float = pa.Field(gt=0)
    disponivel_venda: Bool = pa.Field()
    data_validade: DateTime = pa.Field()

    class Config:
        strict = True

# Função principal do Streamlit app
def main():
    st.title("Validador de Inventário")

    # Widget para upload do arquivo Excel
    uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])
    if uploaded_file is not None:
        # Lendo o arquivo Excel
        df = pd.read_excel(uploaded_file)

        # Tentativa de validação do DataFrame com o esquema
        try:
            # Usando o método validate do schema diretamente pode ser mais direto com DataFrameModel
            new_df = InventarioSchema.validate(df)
            st.write(df)
            st.write(new_df)
            st.success("Validação do esquema bem-sucedida!")
        except pa.errors.SchemaError as e:
            st.error(f"Erro de validação: {e} na linha {e.failure_cases["index"].unique()}")

if __name__ == "__main__":
    main()
