"""
    Serviço:
    1. Coleta via acesso à API da OpenWeatherMap.
        1.1. Execução da coleta e armazenamento no 'db_data' via 'python manage.py coletar_dados --coord <lat> <lon> --api_key <api_key>'.
    
"""
import requests
import pandas as pd
from .models import Cidade, Previsao

# Serviço de coleta de dados climáticos
class ColetaAPI:
    
    def __init__(self, key, lat, lon):
        self.key = key
        self.lat = lat
        self.lon = lon
        self.lang = "pt_br"
        self.units = "metric"
        self.tipo = "forecast"
        self.url_template = 'https://api.openweathermap.org/data/2.5/{tipo}?lat={lat}&lon={lon}&units={units}&lang={lang}&appid={key}'

    def busca_dados(self, lat, lon, tipo):
        
        url = self.url_template.format(tipo=tipo, lat=lat, lon=lon, units=self.units, lang=self.lang, key=self.key)
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Erro ao consumir API: {response.status_code}, {response.text}')
    
    def coleta_dados(self):
        
        data = self.busca_dados(self.lat, self.lon, self.tipo)
        
        # Forecast 
        cidades = []
        previsoes = []

        # Dados da localidade
        localidade = {
            'id_cidade': data['city']['id'],
            'cidade': data['city']['name'],
            'estado': "MS",
            'pais': "BR",
            'coord_lat': data['city']['coord']['lat'],
            'coord_lon': data['city']['coord']['lon'],
            'populacao': data['city']['population'],
            'timezone': data['city']['timezone'],
            'nascer_sol': data['city']['sunrise'],
            'baixar_sol': data['city']['sunset']
        }
        cidades.append(localidade)

        # Dados da previsão
        for previsao in data['list']:
            forecast = {
                'id_cidade': data['city']['id'],
                'data_hora_previsao': previsao['dt_txt'],
                'timestamp_previsao': previsao['dt'],
                'condicao': previsao['weather'][0]['main'],
                'descricao_condicao': previsao['weather'][0]['description'],
                'temperatura': previsao['main']['temp'],
                'max_temp': previsao['main']['temp_max'],
                'min_temp': previsao['main']['temp_min'],
                'sensacao': previsao['main']['feels_like'],
                'umidade': previsao['main']['humidity'],
                'pressao': previsao['main']['pressure'],
                'direcao_vento': previsao['wind']['deg'],
                'velocidade_vento': previsao['wind']['speed']
            }
            previsoes.append(forecast)

        return pd.DataFrame(cidades), pd.DataFrame(previsoes)
    
# Função para executar pela CLI
def coleta_e_armazena_dados(api_key, lat, lon):
    
    coletor = ColetaAPI(api_key, lat, lon)
    df_localidades, df_previsoes = coletor.coleta_dados()
    
    # Convertendo os DataFrames para listas de dicionários
    localidades_data = df_localidades.to_dict(orient='records')
    previsoes_data = df_previsoes.to_dict(orient='records')

    localidades = []
    previsoes = []

    # Enviar ao Postgres | Armazenando as localidades
    for localidade_data in localidades_data:
        cidade, created = Cidade.objects.update_or_create(
            id_cidade=localidade_data['id_cidade'],
            defaults={
                'cidade': localidade_data['cidade'],
                'estado': localidade_data['estado'],
                'pais': localidade_data['pais'],
                'coord_lat': localidade_data['coord_lat'],
                'coord_lon': localidade_data['coord_lon'],
                'populacao': localidade_data['populacao'],
                'timezone': localidade_data['timezone'],
                'nascer_sol': localidade_data['nascer_sol'],
                'baixar_sol': localidade_data['baixar_sol']
            }
        )
        localidades.append(cidade)

    # Enviar ao Postgres | Armazenando as previsões
    for previsao_data in previsoes_data:
        cidade_obj = Cidade.objects.get(id_cidade=previsao_data['id_cidade'])
        previsao, created = Previsao.objects.update_or_create(
            cidade=cidade_obj,
            data_hora_previsao=previsao_data['data_hora_previsao'],
            defaults={
                'timestamp_previsao': previsao_data['timestamp_previsao'],
                'condicao': previsao_data['condicao'],
                'descricao_condicao': previsao_data['descricao_condicao'],
                'temperatura': previsao_data['temperatura'],
                'max_temp': previsao_data['max_temp'],
                'min_temp': previsao_data['min_temp'],
                'sensacao': previsao_data['sensacao'],
                'umidade': previsao_data['umidade'],
                'pressao': previsao_data['pressao'],
                'direcao_vento': previsao_data['direcao_vento'],
                'velocidade_vento': previsao_data['velocidade_vento']
            }
        )
        previsoes.append(previsao)

    return localidades, previsoes

