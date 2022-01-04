from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer, oauth2
from sqlalchemy.orm import Session
from starlette import status
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError

from src.infra.sqlalchemy.repositorios.repositorio_usuarios import RepositorioUsuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    # decodificar o token, pegar o telefone, buscar o usuario no bd e retornar
    try:
        telefone = token_provider.verificar_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token inválido')

    if not telefone:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token inválido')

    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Token inválido')

    return usuario

   
