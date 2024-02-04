from models.user import User as UserModel
from schemas.user import User

class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_users_by_email(self, email):
        result = self.db.query(UserModel).filter(UserModel.email == email).first()
        return result