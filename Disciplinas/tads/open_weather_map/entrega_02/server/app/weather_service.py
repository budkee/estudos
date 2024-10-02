import requests
from datetime import datetime, timedelta
from weather_repository import WeatherRepository
from user_service import UserService


#Servico de coleta de dados climaticos
class OpenWeatherMapClient:
    def __init__(self, api_key):
        self.api_key = '<sua_api_key>'
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather_data(self, latitude, longitude):
        params = {
            'lat': latitude,
            'lon': longitude,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

#formatacao dados pra salvar banco de dados
def parse_weather_data(data):
    return {
        'descricao_weather': data['weather'][0]['description'],
        'temperatura_atual': data['main']['temp'],
        'temperatura_max': data['main']['temp_max'],
        'temperatura_min': data['main']['temp_min'],
        'umidade': data['main']['humidity'],
        'velocidade_vento': data['wind']['speed'],
        'direcao_vento': data['wind']['deg'],
        'rajada_vento': data['wind'].get('gust', 0.0)
    }

### a partir daqui tentei implementar a parte das notificações
class WeatherService:
    def __init__(self):
        self.repo = WeatherRepository()
        self.owm_client = OpenWeatherMapClient(api_key='your_API_key')
        self.user_service = UserService()

#funcao para pegar dados por periodo
    def get_weather_data_by_period(self, start_date, end_date):
        data = self.repo.get_data_by_period(start_date, end_date)
        return data

 
#funcao para enviar notificaçoes

""" 
    def send_notifications(self):
        users = self.user_service.get_all_users()
        for user in users:
            if user.frequency == 'weekly':
                start_date = datetime.utcnow() - timedelta(days=7)
            elif user.frequency == 'biweekly':
                start_date = datetime.utcnow() - timedelta(days=15)
            elif user.frequency == 'monthly':
                start_date = datetime.utcnow() - timedelta(days=30)
            elif user.frequency == 'semiannual':
                start_date = datetime.utcnow() - timedelta(days=182)

            end_date = datetime.utcnow()
            weather_data = self.get_weather_data_by_period(start_date, end_date)
            self.send_email(user.email, weather_data)

#funcao para enviar o email para os usuarios cadastrados
    def send_email(self, to_email, weather_data):
        subject = "Weather Report"
        body = f"Here is your weather report:\n\n{weather_data}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'youremail@example.com'
        msg['To'] = to_email

        with smtplib.SMTP('smtp.example.com') as server: 
            server.login('yourusername', 'yourpassword')
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
"""