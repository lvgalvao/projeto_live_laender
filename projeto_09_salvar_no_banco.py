import streamlit as st

import pandas as pd

from contrato_de_dados import InventarioDoMundoSchema

import sqlite3

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
            st.write(new_df)
            st.success("Validação do esquema bem-sucedida!")
            # Botão para salvar no banco de dados
            if st.button("Salvar no Banco de Dados"):
                # Criando uma conexão com o banco de dados SQLite
                con = sqlite3.connect('inventario.db')
                df_para_validar.to_sql("inventario", con, if_exists='replace', index=False)
                st.success("Dados salvos com sucesso no banco de dados!")
                con.close()
        except Exception as e:
            st.error(f"Erro de validação: {e}")

if __name__ == "__main__":
    main()
