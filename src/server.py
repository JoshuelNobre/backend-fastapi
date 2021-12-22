from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.repositorios.usuarios import RepositorioUsuario
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.repositorios.produtos import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db, criar_bd

criar_bd()

app = FastAPI()

@app.post('/produtos', response_model=ProdutoSimples, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', response_model=List[Produto], status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.post('/usuario', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: Usuario, db:Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
