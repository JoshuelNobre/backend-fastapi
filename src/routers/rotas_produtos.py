from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm.session import Session
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.repositorios.repositorio_produtos import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/produtos', response_model=ProdutoSimples, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@router.get('/produtos', response_model=List[Produto], status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@router.get('/produtos/{id}')
def exibir_produto(id: int, db:Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).buscarPorId(id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Não há um produto com id = {id}')
    return produto_localizado

@router.put('/produtos/{id}', response_model=ProdutoSimples)
def atualizar_produto(id:int, produto: Produto, db:Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto

@router.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return {'msg': 'deletado'}