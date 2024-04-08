from datetime import datetime

def validar_tipos(nome_produto, 
                  quantidade_estoque, 
                  preco_unitario, 
                  disponivel_venda,
                  data):
    # Verifica se 'nome_produto' é uma instância de str (string)
    if not isinstance(nome_produto, str):
        return False
    
    # Verifica se 'quantidade_estoque' é uma instância de int (inteiro)
    if not isinstance(quantidade_estoque, int):
        return False
    
    # Verifica se 'preco_unitario' é uma instância de float (ponto flutuante)
    if not isinstance(preco_unitario, float):
        return False
    
    # Verifica se 'disponivel_venda' é uma instância de bool (booleano)
    if not isinstance(disponivel_venda, bool):
        return False
    
    # Verifica se 'disponivel_venda' é uma instância de bool (booleano)
    if not isinstance(data, datetime):
        return False
    
    # Se todas as verificações passaram, retorna True
    return True

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