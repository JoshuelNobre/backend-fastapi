from fastapi import APIRouter
from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm.session import Session
from src.infra.sqlalchemy.repositorios.repositorio_usuarios import RepositorioUsuario
from src.schemas.schemas import Produto, Usuario, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/signup', response_model=Usuario, status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, db:Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

@router.get('/usuarios', response_model=List[Usuario], status_code=status.HTTP_200_OK)
def listar_usuarios(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios