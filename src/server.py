from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth, rotas_pedidos, rotas_produtos

# RUN
app = FastAPI()

# CORS

origins = ['httpp://localhost:3000']
app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],)

# Rotas produtos
app.include_router(rotas_produtos.router)

# Rotas segurança: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix="/auth")

# Rotas pedidos
app.include_router(rotas_pedidos.router)