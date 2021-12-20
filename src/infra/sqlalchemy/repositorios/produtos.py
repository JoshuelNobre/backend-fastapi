from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class Repositorio():

    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome)

    def listar(self):
        pass

    def obter(self):
        pass

    def remover(self):
        pass

