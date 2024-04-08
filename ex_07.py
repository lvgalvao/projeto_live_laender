nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True

# Simulando a venda de 1 unidade por dia
for dia in range(1, 11):  # Itera do dia 1 ao dia 10
    print(f"--- Dia {dia} ---")
    quantidade_estoque -= 1  # Assume que uma unidade é vendida a cada dia
    print(f"Estoque restante de {nome_produto}: {quantidade_estoque}")
    
    # Verifica a necessidade de reabastecimento do estoque
    if quantidade_estoque <= 5:
        print("Comprar mais estoque")
    else:
        print("Não precisa comprar mais estoque")

    # Imprimindo uma mensagem para separar os dias
    print("Esse bloco é executado a cada iteração do loop\n")