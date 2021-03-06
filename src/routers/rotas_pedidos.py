from fastapi import APIRouter
from fastapi import FastAPI, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm.session import Session
from src.routers.auth_utils import obter_usuario_logado
from src.schemas.schemas import Pedido, Usuario
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()


@router.post('/pedido', status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedido(pedido: Pedido, db: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(db).gravar_pedido(pedido)
    return pedido_criado

@router.get('/pedidos/{id}',response_model=Pedido)
def exibir_pedido(id: int, db: Session = Depends(get_db)):
    try:
        pedido = RepositorioPedido(db).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Não existe pedido com id = {id}')

@router.get('/pedidos', response_model=List[Pedido])
def listar_pedido(usuario_id: Usuario=Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar_meus_pedidos_por_usuario_id(usuario_id)
    return pedidos  

@router.get('/pedidos/{usuario_id}/vendas', response_model=List[Pedido])
def listar_vendas(usuario_id:int, db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar_minhas_vendas_por_usuario_id(usuario_id)
    return pedidos  
