from flask import Flask, request, jsonify, make_response
from flask_restx import Api, Resource, fields
from user_service import UserService
from models_user import User
from weather_service import WeatherService, OpenWeatherMapClient, parse_weather_data
from weather_repository import WeatherRepository
from models import Session

app = Flask(__name__)
api = Api(app, version='1.0', title='Weather Data API',
          description='A simple Weather Data API')

weather_service = WeatherService()

ns = api.namespace('weather', description='Weather operations')

API_KEY = 'your_API_key'

location_model = api.model('Location', {
    'latitude': fields.Float(required=True, description='The latitude'),
    'longitude': fields.Float(required=True, description='The longitude'),
    'nome': fields.String(description='The name of the location')
})

weather_data_model = api.model('WeatherData', {
    'data_hora': fields.DateTime(description='Timestamp of the data'),
    'localizacao': fields.Nested(api.model('Localizacao', {
        'latitude': fields.Float(description='The latitude'),
        'longitude': fields.Float(description='The longitude'),
        'nome': fields.String(description='The name of the location')
    })),
    'descricao_weather': fields.String(description='Weather description'),
    'temperatura_atual': fields.Float(description='Current temperature'),
    'temperatura_max': fields.Float(description='Maximum temperature'),
    'temperatura_min': fields.Float(description='Minimum temperature'),
    'umidade': fields.Float(description='Humidity'),
    'velocidade_vento': fields.Float(description='Wind speed'),
    'direcao_vento': fields.Float(description='Wind direction'),
    'rajada_vento': fields.Float(description='Wind gust speed')
})

pagination_model = api.model('Pagination', {
    'limit': fields.Integer(description='Limit of records per page'),
    'page': fields.Integer(description='Page number')
})

#Swagger
#POST rota /weather/collect, respostas 201 sucesso e 400 falha
@ns.route('/collect', methods = ['POST'])
class CollectWeatherData(Resource):
    @ns.expect(location_model)
    @ns.response(201, 'Weather data collected successfully')
    @ns.response(400, 'Invalid input')
    def post(self):
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        nome = data.get('nome', 'Unknown')

        if not latitude or not longitude:
            return jsonify({"error": "Latitude and longitude are required"}), 400

        owm_client = OpenWeatherMapClient('792c01f811455c6aaf9ecad74a3f8b01')
        weather_data = owm_client.get_weather_data(latitude, longitude)
        parsed_data = parse_weather_data(weather_data)

        repo = WeatherRepository()
        localizacao = {"latitude": latitude, "longitude": longitude, "nome": nome}
        saved_localizacao = repo.save_localizacao(localizacao)
        repo.save_condicoes_climaticas(saved_localizacao.id, parsed_data)

        return {"message": "Weather data collected successfully"}, 201


#GET rota weather/data limite de 10 registros por pagina

@ns.route('/data', methods = ['GET'])
class ListWeatherData(Resource):
    @ns.expect(pagination_model)
    @ns.marshal_list_with(weather_data_model)
    def get(self):
        try:
            limit = int(request.args.get('limit', 10))
            page = int(request.args.get('page', 1))
        except ValueError:
            return jsonify({"error": "Invalid limit or page parameter"}), 400

        offset = (page - 1) * limit
        repo = WeatherRepository()
        data = repo.get_paginated_data(limit, offset)

        result = []
        for record in data:
            result.append({
                'data_hora': record.data_hora,
                'localizacao': {
                    'latitude': record.localizacao.latitude,
                    'longitude': record.localizacao.longitude,
                    'nome': record.localizacao.nome
                },
                'descricao_weather': record.descricao_weather,
                'temperatura_atual': record.temperatura_atual,
                'temperatura_max': record.temperatura_max,
                'temperatura_min': record.temperatura_min,
                'umidade': record.umidade,
                'velocidade_vento': record.velocidade_vento,
                'direcao_vento': record.direcao_vento,
                'rajada_vento': record.rajada_vento
            })

        return result, 200


#### aqui comeca o endpoint para notificao dos usuarios

user_notification_model = api.model('UserNotification', {
    'message': fields.String(required=True, description='Notification message to send')
})


@ns.route('/notify', methods=['POST'])
class NotifyUsers(Resource):
    @ns.expect(user_notification_model)
    @ns.response(200, 'Notifications sent successfully')
    @ns.response(400, 'Invalid input')
    def post(self):
        data = request.get_json()
        msg = data.get('message')

        if not msg:
            return {'error': 'Message is required'}, 400

        weather_service = WeatherService()
        weather_service.send_notifications()

        return {'message': 'Notifications sent successfully'}, 200

if __name__ == '__main__':
    app.run(debug=True)
