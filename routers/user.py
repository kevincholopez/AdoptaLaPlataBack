from fastapi import APIRouter
from pydantic import BaseModel
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
from config.database import Session
from services.user import UserService

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User):
    db = Session()
    result = UserService(db).get_users_by_email(user.email)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No existe un usuario registrado"})
    if user.password == result.password:
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    else:
        return JSONResponse(status_code=500, content={'message': "Contraseña incorrecta, intente nuevamente"})