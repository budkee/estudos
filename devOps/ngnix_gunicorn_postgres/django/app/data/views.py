import os
import json
# -------- Django Framework -----------------
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# -------- REST Framework -----------------
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
# -------- Data App -----------------
from .models import Cidade, Previsao
from .serializers import PrevisaoSerializer, CidadeSerializer
from .services import ColetaAPI

# ----------------- Visões -----------------------
class DataViewSet(viewsets.ViewSet):
    
    # @action(detail=True, methods=['post'], url_path='collect')
    @api_view(['GET'])
    def recupera_dados(self, request):
        previsoes = Previsao.objects.using('db_data').all()[offset:offset + limit]
        limit = int(request.query_params.get('limit', 10))
        page = int(request.query_params.get('page', 1))
        offset = (page - 1) * limit
        serializer = PrevisaoSerializer(previsoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=True, methods=['get'], url_path='data')
    @api_view(['POST'])
    def coleta(self, request):
        
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not latitude or not longitude:
            return Response({"error": "Latitude and longitude are required"}, status=status.HTTP_400_BAD_REQUEST)

        api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        coleta_api = ColetaAPI(api_key, latitude, longitude)
        
        try:
            df_localidades, df_previsoes = coleta_api.coleta_dados()

            for _, localidade_data in df_localidades.iterrows():
                cidade, created = Cidade.objects.using('db_data').get_or_create(
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
                        'baixar_sol': localidade_data['baixar_sol'],
                    }
                )

            for _, previsao_data in df_previsoes.iterrows():
                Previsao.objects.using('db_data').create(
                    cidade=Cidade.objects.using('db_data').get(id_cidade=previsao_data['id_cidade']),
                    data_hora_previsao=previsao_data['data_hora_previsao'],
                    timestamp_previsao=previsao_data['timestamp_previsao'],
                    condicao=previsao_data['condicao'],
                    descricao_condicao=previsao_data['descricao_condicao'],
                    temperatura=previsao_data['temperatura'],
                    max_temp=previsao_data['max_temp'],
                    min_temp=previsao_data['min_temp'],
                    sensacao=previsao_data['sensacao'],
                    umidade=previsao_data['umidade'],
                    pressao=previsao_data['pressao'],
                    direcao_vento=previsao_data['direcao_vento'],
                    velocidade_vento=previsao_data['velocidade_vento']
                )

            return Response({"message": "Weather data collected successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    