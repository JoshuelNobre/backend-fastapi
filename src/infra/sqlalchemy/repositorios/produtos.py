from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db
    
    # def criar(self, produto: schemas.Produto):
    #     db_produto = models.Produto(**produto.dict())
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel,
                                    usuario_id=produto.usuario_id)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def editar(self, produto: schemas.Produto):
        updated_stmt = update(models.Produto).where(models.Produto.id == produto.id).values(**produto.dict())
        self.db.execute(updated_stmt)
        self.db.commit()

    def remover(self):
        pass

# schemas = vai e volta do request
# models = vai e volta do banco de dados 