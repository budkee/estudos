"""
    # Nível 1: Conexão com o servidor PostgreSQL (OK)
    # Nível 2: Criação de tabelas(localidades, previsoes) via GUI
    # Nível 3: Inserção de dados via script
    # Nível 4: Recuperação de dados via script
    Vídeo: https://www.youtube.com/results?search_query=conectar+o+postgresql+via+script
"""
    
# Imports
import os
from sqlalchemy import create_engine, Engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

# Conexão com o servidor PostgreSQL
## Declaração das variáveis de ambiente
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '100.113.19.15')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5433')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'gatinho_estrelar')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')

## URL de conexão com PostgreSQL no Docker
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    
# Setting up SQLAlchemy
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

# Definição das classes e entidades
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)

    @classmethod
    def create_user(cls, name, email, age):
        """Insert a new user into the users table."""
        session = Session()
        new_user = cls(name=name, email=email, age=age)  # Aqui cls é usado para criar uma nova instância da classe User
        session.add(new_user)
        session.commit()
        session.close()

    @classmethod
    def read_users(cls):
        """Query all rows in the users table."""
        session = Session()
        users = session.query(cls).all()  # Aqui cls é usado para consultar todos os registros da tabela associada à classe User
        for user in users:
            print(user.id, user.name, user.email, user.age)
        session.close()

    @classmethod
    def update_user(cls, user_id, new_age):
        """Update age of a user."""
        session = Session()
        user = session.query(cls).filter(cls.id == user_id).first()  # Aqui cls é usado para filtrar um registro específico na tabela
        if user:
            user.age = new_age
            session.commit()
        session.close()

    @classmethod
    def delete_user(cls, user_id):
        """Delete a user by user id."""
        session = Session()
        user = session.query(cls).filter(cls.id == user_id).first()  # Aqui cls é usado para filtrar um registro específico na tabela
        if user:
            session.delete(user)
            session.commit()
        session.close()

def main():
    # Tentando conectar ao banco de dados
    try:
        connection = engine.connect() # type: ignore
        print("Conexão com o PostgreSQL estabelecida com sucesso!")
        connection.close()
    except Exception as e:
        print(f"Falha ao conectar com o PostgreSQL: {e}")
        return

    # Criar a sessão
    session = Session()

    # Create tables
    Base.metadata.create_all(engine)

    # CRUD
    # Create a new user
    User.create_user('David Wright', 'david.wright@example.com', 28)
    print("User created.")

    # Read users
    print("Users in the database:")
    User.read_users()

    # Update user's age
    User.update_user(1, 29)
    print("User updated.")

    # Read users
    print("Users in the database after update:")
    User.read_users()

    # Delete user
    # User.delete_user(1)
    # print("User deleted.")

    # # Read users
    # print("Users in the database after deletion:")
    # User.read_users()

    # Fechar a sessão
    session.close()

if __name__ == "__main__":
    main()