from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

# ----------- Conexão com o BD ----------- 

# Criação do banco de dados Usuarios
DATABASE_URL_USER = 'postgresql+psycopg2://postgres:admin@100.113.19.15:5433/user_db'

engine_user = create_engine(DATABASE_URL_USER)
SessionUser = sessionmaker(bind=engine_user)
Base = declarative_base()

# Criacao da tabela usuarios com os atributos id, email e frequencia

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    frequency = Column(String, nullable=False)

Base.metadata.create_all(bind=engine_user)
