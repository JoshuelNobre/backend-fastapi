from datetime import datetime, timedelta
from jose import jwt

#CONFIG
SECRET_KEY = 'caa9c8f8620cbb30679026bb6427e11f'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_acess_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp':expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY,algorithm=ALGORITHM)
    return token_jwt

def verificar_acess_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[SECRET_KEY])
    return carga.get('sub')