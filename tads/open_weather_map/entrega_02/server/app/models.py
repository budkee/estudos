from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime


# DATABASE_URL_WEATHER = 'postgresql+psycopg2://postgres:admin@localhost/weather_db'
DATABASE_URL_WEATHER = 'postgresql+psycopg2://postgres:admin@100.113.19.15:5433/weather_db'

engine_weather = create_engine(DATABASE_URL_WEATHER)
Session = sessionmaker(bind=engine_weather)
Base = declarative_base()

#criacao entidades e agregados (DDD)

class Localizacao(Base):
    __tablename__ = 'localizacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    nome = Column(String, nullable=True)
    condicoes_climaticas = relationship('CondicoesClimaticas', back_populates='localizacao')

class CondicoesClimaticas(Base):
    __tablename__ = 'condicoes_climaticas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_hora = Column(DateTime, default=datetime.utcnow)
    descricao_weather = Column(String)
    temperatura_atual = Column(Float)
    temperatura_max = Column(Float)
    temperatura_min = Column(Float)
    umidade = Column(Float)
    velocidade_vento = Column(Float)
    direcao_vento = Column(Float)
    rajada_vento = Column(Float)
    localizacao_id = Column(Integer, ForeignKey('localizacao.id'))
    localizacao = relationship('Localizacao', back_populates='condicoes_climaticas')

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine_weather)
