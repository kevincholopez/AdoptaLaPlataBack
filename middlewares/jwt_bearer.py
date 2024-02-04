
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_manager import create_token, validate_token
from services.user import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        db = Session()
        result = UserService(db).get_users_by_email(data['email'])
        if not result:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")