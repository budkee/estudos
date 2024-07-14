from rest_framework import serializers
from .models import Cidade, Previsao

class CidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cidade
        fields = '__all__'

class PrevisaoSerializer(serializers.ModelSerializer):
    
    # cidade = CidadeSerializer(read_only=True)  # Nested serializer to include city details
    
    ## Define o modelo e os campos a serem serializados
    class Meta:
        model = Previsao
        fields = '__all__'
