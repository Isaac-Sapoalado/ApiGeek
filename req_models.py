from pydantic import BaseModel

class Req_Produto(BaseModel):
    
    nome: str
    preco: float = 1
    quantidade_estoque: int = 1
    descricao: str | None = None
    categoria: str | None = None
    franquia: str | None = None

class Req_Estoque(BaseModel):

    tipo: str
    quantidade: int