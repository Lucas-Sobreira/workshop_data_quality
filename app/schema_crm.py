import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchemaEmail(pa.DataFrameModel):
    """
    Define o esquema para a validação de dados de produtos com Pandera.
    
    Este esquema inclui campos básicos para produtos, incluindo um campo de e-mail
    validado por uma expressão regular.

    Attributes:
        id_produto (Series[int]): Identificador do produto, deve estar entre 1 e 20.
        nome (Series[str]): Nome do produto.
        quantidade (Series[int]): Quantidade disponível do produto, deve estar entre 20 e 200.
        preco (Series[float]): Preço do produto, deve estar entre 5.0 e 120.0.
        categoria (Series[str]): Categoria do produto.
        email (Series[str]): E-mail associado ao produto, deve seguir o formato padrão de e-mails.
    """
    id_produto: Series[int] = pa.Field(ge=1, le=100)
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=5.0, le=120.0)
    categoria: Series[str]
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True # Força conversão de tipos
        strict = True # Permite colunas extras