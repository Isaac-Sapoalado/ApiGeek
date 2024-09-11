from sqlmodel import Field,SQLModel
from typing import Optional
from sqlalchemy import table

class Produto(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: int
    categoria: Optional[str] = None
    franquia: Optional[str] = None

    #obrigatorios : (nome,preco,quantidade)
