from pydantic import BaseModel
from typing import Optional, List


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    nome: str
    preco: float

    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    senha: str
    telefone: str
    produtos: List[ProdutoSimples] = []
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]
    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]

    class Config:
        orm_mode = True

# class Pedido(BaseModel):
#     id: Optional[str] = None
#     usuario: Usuario
#     # produto: Produto
#     quantidade: int
#     entrega: bool = False
#     endereco: str
#     observacoes: Optional[str] = 'Sem observações'
