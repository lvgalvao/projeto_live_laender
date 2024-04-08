from datetime import datetime

from modulo_de_validar import validar_tipos

# Testando a função com os valores fornecidos
nome_produto = "Mesa de Escritório"
quantidade_estoque = 10
preco_unitario = 450.0
disponivel_venda = True
data = datetime(2023,12,31)

# Chamada à função com as variáveis como argumentos
resultado = validar_tipos(nome_produto, quantidade_estoque, preco_unitario, disponivel_venda, data)

# Imprime o resultado da validação
print("Todos os tipos são válidos?" , resultado)