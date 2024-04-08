nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True

if quantidade_estoque <= 5:
    # Faça determinada coisa....
    print("Comprar mais estoque")
else:
    print("Não precisa comprar mais estoque")

print("Esse bloco")