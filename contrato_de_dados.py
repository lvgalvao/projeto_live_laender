from pandera import DataFrameModel, Field

from pandera.typing import DateTime, String, Int, Float, Bool

class InventarioDoMundoSchema(DataFrameModel):
    """
    Representa um contrato de dados para um produto em um sistema de gerenciamento de inventário.

    Esta classe define a estrutura de dados para produtos, incluindo informações sobre o nome do produto,
    a quantidade em estoque, o preço unitário, se o produto está disponível para venda, e a data de validade do produto.

    Attributes:
        nome_produto (str): O nome do produto, como 'Mesa de Escritório'.
        quantidade_estoque (int): A quantidade do produto disponível em estoque.
        preco_unitario (float): O preço unitário do produto.
        disponivel_venda (bool): Um valor booleano indicando se o produto está disponível para venda.
        data_validade (datetime): A data de validade do produto.
    """
    nome_produto: String = Field()
    quantidade_estoque: Int = Field()
    preco_unitario: Float = Field()
    disponivel_venda: Bool = Field()
    data_validade: DateTime = Field()

    class Config:
        strict = True  # Garante que apenas as colunas definidas estão presentes
