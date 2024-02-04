from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class User(Base):

    __tablename__ = "Usuario"
    
    idUsuario = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    vigente = Column(Integer)