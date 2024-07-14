import os
from django.core.management.base import BaseCommand
from data.services import coleta_e_armazena_dados

class Command(BaseCommand):
    help = 'Coleta e armazena dados meteorológicos com base em coordenadas geográficas.'

    def add_arguments(self, parser):
        parser.add_argument('--coord', nargs=2, metavar=('lat', 'lon'), required=True, help='Latitude e longitude da estação meteorológica de interesse.')
        # parser.add_argument('--api_key', required=True, help='Chave da API do OpenWeatherMap.')

    def handle(self, *args, **options):
        lat = float(options['coord'][0])
        lon = float(options['coord'][1])
        api_key = os.getenv('OPENWEATHERMAP_API_KEY')

        if not api_key:
            raise CommandError('A chave da API não está configurada.')

        coleta_e_armazena_dados(api_key, lat, lon)
