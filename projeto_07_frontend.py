import streamlit as st

import pandas as pd

from contrato_de_dados import InventarioDoMundoSchema


def main():
    st.title("Validador de Inventário")

    # Widget para upload do arquivo Excel
    uploaded_file = st.file_uploader("Escolha um arquivo Excel", type=["xlsx"])
    if uploaded_file is not None:
        # Lendo o arquivo Excel
        df_para_validar = pd.read_excel(uploaded_file)

        # Tentativa de validação do DataFrame com o esquema
        try:
            new_df = InventarioDoMundoSchema.validate(df_para_validar)
            print(new_df)
            print("Validação do esquema bem-sucedida!")
        except Exception as e:
            print(f"Erro de validação: {e}")

if __name__ == "__main__":
    main()
