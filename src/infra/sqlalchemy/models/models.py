from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)

class Usuario(Base):

    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    telefone = Column(String, index=True)

