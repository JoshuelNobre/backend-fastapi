from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.traversals import STATIC_CACHE_KEY
from sqlalchemy.util.langhelpers import _hash_limit_string
from src.infra.sqlalchemy.repositorios.repositorio_usuarios import RepositorioUsuario
from src.schemas.schemas import LoginSucesso, Produto, Usuario, ProdutoSimples, LoginData, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider, token_provider
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post('/signup', response_model=UsuarioSimples, status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, db:Session = Depends(get_db)):
    # verificar se já existe um usuário para o telefone
    usuario_localizado = RepositorioUsuario(db).obter_por_telefone(usuario.telefone)

    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Já existe um usuário para este telefone')

    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

# @router.get('/usuarios', response_model=List[Usuario], status_code=status.HTTP_200_OK)
# def listar_usuarios(db:Session = Depends(get_db)):
#     usuarios = RepositorioUsuario(db).listar()
#     return usuarios

@router.post('/token', response_model=LoginSucesso)
def login(login_data: LoginData, db:Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Telefone ou senha estão incorretos')

    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Telefone ou senha estão incorretos')
    
    #Gerar token JWT
    token = token_provider.criar_acess_token({'sub': usuario.telefone})
    return LoginSucesso (usuario=usuario, acess_token=token)

@router.get('/me', response_model=UsuarioSimples)
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario