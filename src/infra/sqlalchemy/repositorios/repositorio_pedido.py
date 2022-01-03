from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete, select
from sqlalchemy.sql.functions import mode
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import update, delete
from typing import List

class RepositorioPedido():

    def  __init__(self, db: Session):
        self.db = db

    def gravar_pedido(self, pedido: schemas.Pedido):
        pedido_db = models.Pedido(quantidade = pedido.quantidade,
                                    local_entrega = pedido.local_entrega,
                                    tipo_entrega = pedido.tipo_entrega,
                                    observacao = pedido.observacao,
                                    usuario_id = pedido.usuario_id,
                                    produto_id = pedido.produto_id
                                    )
        self.db.add(pedido_db)
        self.db.commit()
        self.db.refresh(pedido_db)
        return pedido_db

    def buscar_por_id(self, id:int):
        query = select(models.Pedido).where(models.Pedido.id == id)
        resultado = self.db.execute(query).one()
        return resultado[0]

    def listar_meus_pedidos_por_usuario_id(self, usuario_id:int):
        query = select(models.Pedido).where(models.Pedido.usuario_id == usuario_id)
        resultado = self.db.execute(query).scalars().all()
        return resultado

    def listar_minhas_vendas_por_usuario_id(self, usuario_id:int):
        query = select(models.Pedido)\
            .join_from(models.Pedido, models.Produto)\
            .where(models.Produto.usuario_id == usuario_id)
        resultado = self.db.execute(query).scalars().all()
        return resultado


