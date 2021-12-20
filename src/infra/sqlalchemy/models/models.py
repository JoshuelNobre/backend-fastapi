from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

class Produto():

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(Integer, primary_key=True, index=True)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)