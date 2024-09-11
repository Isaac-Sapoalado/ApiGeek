from database import get_engine,sync_database
from db_models import Produto
from sqlmodel import Session, select


class Produto_service():

    def __init__(self):

        engine = get_engine()
        self.session = Session(engine)


    def get_produto_id(self,id: int):

        fecth = select(Produto).where(Produto.id==id)
        return self.session.exec(fecth).one_or_none()
    
    def get_produto_all(self):

        fecth = select(Produto)
        return self.session.exec(fecth).all()
    
    def post_produto(self,produto:Produto):

        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto
    
    def put_produto(self,produto:Produto,id:int):
        
        db_produto = self.get_produto_id(id=id)
        if (produto.nome != db_produto.nome) and produto.nome:
            db_produto.nome = produto.nome
        if (produto.preco != db_produto.preco) and produto.preco:
            db_produto.preco = produto.preco
        if (produto.quantidade_estoque != db_produto.quantidade_estoque) and produto.quantidade_estoque:
            if produto.quantidade_estoque < 0:
                return False
            db_produto.quantidade_estoque = produto.quantidade_estoque
        if (produto.descricao != db_produto.descricao) and produto.descricao:
            db_produto.descricao = produto.descricao
        if (produto.categoria != db_produto.categoria) and produto.categoria:
            db_produto.categoria = produto.categoria
        if (produto.franquia != db_produto.franquia) and produto.franquia:
            db_produto.franquia = produto.franquia

        self.session.add(produto)
        self.session.commit()
        self.session.refresh(produto)
        return produto

    
    def delete_produto(self,id:int):

        fecth = select(Produto).where(Produto.id == id)
        result = self.session.exec(fecth)
        produto = result.one_or_none()
        if not produto:
            return False
        if produto.quantidade_estoque == 0:
            return False
        self.session.delete(produto)
        self.session.commit()
        return produto

#Produtos só podem ser excluídos se estiverem fora de estoque.V
#Ao atualizar a quantidade em estoque de um produto, a API deve impedir a inserção de valores negativos.V
#Não é possível vender se não tiver Estoque. Reposição incrementa a quantidade.V
