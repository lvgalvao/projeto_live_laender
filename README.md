## O que é Python?

## Por quê usar Python?

## O que dâ para fazer com Python?

## Como instalar Python?

https://studio.youtube.com/video/9LYqtLuD7z4

## O que são Variáveis?

Em programação, uma variável é um nome que é associado a um valor. 

Variáveis são fundamentais na maioria das linguagens de programação, incluindo Python, pois permitem o armazenamento e manipulação de dados. 

O valor de uma variável pode ser alterado ao longo do programa, o que oferece flexibilidade e controle sobre como os dados são manipulados e apresentados.

## Tipos Simples em Python

Python é uma linguagem dinamicamente tipada, o que significa que você não precisa declarar explicitamente os tipos de variáveis ao criá-las. No entanto, vamos fazer isso porque é uma boa prática a para dados tipos é muito importante.

```python
nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True
```

## O que são Funções?

Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas podem aceitar entradas (também conhecidas como argumentos ou parâmetros), processar essas entradas e retornar um resultado. Funções são fundamentais na programação, pois ajudam a organizar o código, tornando-o mais legível, manutenível e modular. 

### Exemplo de Função: `print()`

```python
# Imprime uma mensagem simples
print("ola mundo!")
print(nome_produto)
print(f"meu produto é o: {nome_produto}")
```

### Exemplo de Função: `input()`

A função `input()` permite capturar entrada do usuário. Ela exibe uma mensagem opcional ao usuário e espera que o usuário digite algo. Quando o usuário pressiona Enter, a função retorna o texto digitado como uma string.

**Uso:**

```python
# Pede ao usuário para digitar seu nome e armazena o resultado na variável nome_usuario
nome_usuario = input("Digite seu nome: ")
print("Olá,", nome_usuario + "!")
```

Neste exemplo, `input("Digite seu nome: ")` exibe a mensagem "Digite seu nome: " e aguarda a entrada do usuário. Quando o usuário digita seu nome e pressiona Enter, esse valor é armazenado na variável `nome_usuario`, que é então usada na função `print()` para saudar o usuário pelo nome.

### Conclusão

Funções são componentes essenciais na programação Python, oferecendo uma maneira de encapsular lógicas de programação em blocos reutilizáveis e modulares. Elas permitem que os programadores organizem melhor seu código, tornem-no mais legível e facilitem a depuração e manutenção. As funções embutidas como `print()` e `input()` são apenas exemplos do vasto conjunto de funcionalidades que o Python oferece para facilitar a interação com o usuário e a manipulação de dados.

### Exemplo de Uso da Função `type()`

```python
numero = 42
texto = "Olá, mundo!"
booleano = True

print(type(numero))  # <class 'int'>
print(type(texto))   # <class 'str'>
print(type(booleano))  # <class 'bool'>
```

Neste exemplo, `type()` é usado para imprimir o tipo de várias variáveis. O resultado mostra que `numero` é do tipo `int`, `texto` é do tipo `str`, e `booleano` é do tipo `bool`.

## O que são Métodos?

Métodos são funções associadas a objetos que podem manipular os dados contidos nesses objetos ou realizar operações específicas relacionadas a eles. Em Python, cada tipo de dado tem seus próprios métodos integrados, permitindo realizar operações comuns de forma conveniente e eficaz. Vamos explorar um exemplo de método para cada um dos tipos básicos mencionados:

### Métodos para Strings (`str`)

**Método:** `.upper()`

Este método retorna uma nova string com todos os caracteres em maiúsculas.

```python
nome_produto: str = "Mesa de Escritório"
nome_produto_maiusculo = nome_produto.upper()
print(nome_produto_maiusculo)  # Output: MESA DE ESCRITÓRIO
```

## O Tipo DateTime

* **Datetime**: Diferente dos tipos anteriores, `datetime` não é um tipo de dado primitivo em Python, mas sim uma classe disponível no módulo `datetime`, que é parte da biblioteca padrão do Python. Objetos `datetime` são usados para representar informações de data e hora.
    
    Por não ser um tipo primitivo, para usar `datetime`, você precisa primeiro importar o módulo `datetime`:
    
    ```python
    from datetime import datetime
    ```

### Até agora não conseguimos manipular o Python

### Exemplo de Uso do `if`

Suponha que você tenha um programa que deve exibir uma mensagem baseada na idade do usuário:

```python
if quantidade_estoque <= 5:
    # Faça determinada coisa....
    print("Comprar mais estoque")
else:
    print("Não precisa comprar mais estoque")

print("Esse bloco")
```

Neste exemplo, o programa pede ao usuário para digitar sua idade. Em seguida, usa-se o `if` para verificar se a idade é maior ou igual a 18. Se a condição for verdadeira (ou seja, se o usuário tiver 18 anos ou mais), o programa exibe "Você é maior de idade." Caso contrário, o bloco de código após o `else` é executado, e o programa exibe "Você é menor de idade."

## Uso do FOR

O loop `for` em Python é uma ferramenta poderosa e flexível usada para iterar sobre os elementos de uma sequência ou qualquer outro objeto iterável.

### Definindo e Chamando Funções

Para definir uma função:

```python
def minha_funcao():
    print("Olá, mundo!")
```

Para chamá-la:

```python
minha_funcao()  # Saída: Olá, mundo!
```

Funções podem aceitar parâmetros e retornar valores. Os parâmetros permitem que você passe dados para a função, e o `return` permite que a função envie dados de volta ao chamador.

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # Saída: 8
```

### Importando seus Próprios Módulos

Um módulo em Python é simplesmente um arquivo contendo definições de funções, classes e variáveis, além de código executável. Módulos ajudam a organizar funções, classes e outros elementos em arquivos separados, facilitando a manutenção e a reutilização de código.

Para usar funções definidas em um módulo, você primeiro precisa importá-lo. Suponha que você tenha um arquivo chamado `meu_modulo.py` com a seguinte função:

```python
# Arquivo: meu_modulo.py
def cumprimentar(nome):
    print(f"Olá, {nome}!")
```

Para usar a função `cumprimentar` em outro arquivo Python, você deve importar `meu_modulo` usando a palavra-chave `import`:

```python
# Importa todo o módulo
import meu_modulo

# Agora você pode chamar a função cumprimentar
meu_modulo.cumprimentar("Alice")  # Saída: Olá, Alice!
```

Ou, você pode importar apenas a função específica que deseja usar:

```python
# Importa uma função específica do módulo
from meu_modulo import cumprimentar

# Chama a função diretamente
cumprimentar("Bob")  # Saída: Olá, Bob!
```

## O nosso desafio.... como trabalhar com Excel?

```bash
pip install pandas openpyxl
```

### 2. Filtrando Dados

Vamos filtrar produtos que estão disponíveis para venda e têm quantidade de estoque menor que 10.

```python
disponiveis_e_baixo_estoque = df[(df["disponivel_venda"] == True) & (df["quantidade_estoque"] < 10)]
print(disponiveis_e_baixo_estoque)
```

### 3. Calculando o Valor Total em Estoque

Para cada produto, podemos calcular o valor total em estoque multiplicando a `quantidade_estoque` pelo `preco_unitario`. Depois, somamos todos os valores para obter o total.

```python
df["valor_total_estoque"] = df["quantidade_estoque"] * df["preco_unitario"]
valor_total = df["valor_total_estoque"].sum()
print("Valor total em estoque:", valor_total)
```

### 4. Ordenando os Produtos por Preço Unitário

Para visualizar os produtos do mais caro ao mais barato, podemos ordenar o DataFrame pelo `preco_unitario`.

```python
ordenado_por_preco = df.sort_values(by="preco_unitario", ascending=False)
print(ordenado_por_preco)
```

### 5. Agrupando e Contando Produtos por Disponibilidade

Podemos querer saber quantos produtos estão disponíveis para venda versus quantos não estão.

```python
contagem_por_disponibilidade = df["disponivel_venda"].value_counts()
print(contagem_por_disponibilidade)
```


### Como validar o meu Dataframe????

Procurar no Google...

Criar nosso contrato - Projeto 02
Refatorar e testar - Projeto 03
Erro sem coluna - Projeto 04
Erro com coluna extra - Projeto 05

### E frontend??? Da para fazer????

### E da para salvar no banco de dados???

            if st.button("Salvar no Banco de Dados"):
                # Criando uma conexão com o banco de dados SQLite
                con = sqlite3.connect('inventario.db')
                df_para_validar.to_sql("inventario", con, if_exists='replace', index=False)
                st.success("Dados salvos com sucesso no banco de dados!")
                con.close()

### E a documentacao???

### Instalação

Essas ferramentas são instaladas usando pip, o gerenciador de pacotes do Python. Abra seu terminal e execute os seguintes comandos:

```bash
pip install mkdocs
pip install mkdocs-material
pip install mkdocstrings
pip install mkdocstrings_handlers
```

### Configurando o MkDocs

Após a instalação, você pode configurar seu projeto MkDocs. Primeiro, crie um novo projeto MkDocs executando:

```bash
mkdocs new nome_do_seu_projeto
```

Isso criará um novo diretório com o nome `nome_do_seu_projeto`, contendo um arquivo de configuração básico `mkdocs.yml` e um diretório `docs` para seus arquivos de markdown.

### Configuração do Tema e do mkdocstrings

Para usar o tema Material e o `mkdocstrings`, você precisará editar o arquivo `mkdocs.yml` no diretório raiz do seu projeto MkDocs. Aqui está um exemplo de como configurar ambos:

```yaml
site_name: Nome do Seu Projeto
theme:
  name: 'material'

plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          rendering:
            show_source: true
```