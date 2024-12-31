from models import Localizacao, CondicoesClimaticas, Session

#repositorio de dados climaticos
class WeatherRepository:
    def __init__(self):
        self.session = Session()

    def save_localizacao(self, localizacao):
        loc = Localizacao(**localizacao)
        self.session.add(loc)
        self.session.commit()
        return loc

    def save_condicoes_climaticas(self, localizacao_id, condicoes):
        condicoes['localizacao_id'] = localizacao_id
        cond = CondicoesClimaticas(**condicoes)
        self.session.add(cond)
        self.session.commit()
        return cond

    def get_paginated_data(self, limit, offset):
        query = self.session.query(CondicoesClimaticas).offset(offset).limit(limit).all()
        return query


    #dados por periodo

    def get_data_by_period(self, start_date, end_date):
        query = self.session.query(CondicoesClimaticas).filter(
            CondicoesClimaticas.data_hora.between(start_date, end_date)
        ).all()
        return query
