from fastapi import APIRouter,status,HTTPException
from req_models import Req_Produto
from services import Produto_service
from db_models import Produto
from utils import calcular_preco

rota = APIRouter()

service_produto = Produto_service()

@rota.get('/',response_model=list[Produto])
def pegar():
    return service_produto.get_produto_all()

@rota.get('/{id}',response_model=Produto)
def pegar_id(id:int):
    pr = service_produto.get_produto_id(id=1)
    produto = service_produto.get_produto_id(id=id)
    if produto:
        return produto
    raise HTTPException(status.HTTP_404_NOT_FOUND,"produto não existe")


@rota.post('/',response_model=Produto)
def criar(requisicao:Req_Produto):
    produto = Produto(
        nome=requisicao.nome,
        descricao=requisicao.descricao,
        preco=calcular_preco(requisicao.preco),
        quantidade_estoque=requisicao.quantidade_estoque,
        categoria=requisicao.categoria,
        franquia=requisicao.franquia
        )
    return service_produto.post_produto(produto=produto)

@rota.put('/{id}', response_model=Produto)
def atualizar(id:int,requisicao:Req_Produto):

    produto = Produto(
        nome=requisicao.nome,
        descricao=requisicao.descricao,
        preco=requisicao.preco,
        quantidade_estoque=requisicao.quantidade_estoque,
        categoria=requisicao.categoria,
        franquia=requisicao.franquia
        )
    
    result = service_produto.put_produto(produto=produto,id=id)
    if not result:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,"não são aceitos valores negativos no atributo 'quantidade_estoque'")
    return result


@rota.delete('/{id}',response_model=Produto)
def deletar(id:int):
    result = service_produto.delete_produto(id=id)
    if not result:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE,"atributo 'quantidade_estoque' maior que zero ou não existe")
    return result