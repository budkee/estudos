from django.db import models

class Cidade(models.Model):
    
    id_cidade = models.IntegerField(primary_key=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=2)
    coord_lat = models.FloatField()
    coord_lon = models.FloatField()
    populacao = models.IntegerField()
    timezone = models.IntegerField()
    nascer_sol = models.IntegerField()
    baixar_sol = models.IntegerField()

    class Meta:
        app_label = 'data'  # Define o nome do aplicativo

    def __str__(self):
        return f"{self.cidade} | Coordenadas:({self.coord_lat}, {self.coord_lon})"

class Previsao(models.Model):
    
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data_hora_previsao = models.CharField(max_length=20)
    timestamp_previsao = models.IntegerField()
    condicao = models.CharField(max_length=50)
    descricao_condicao = models.CharField(max_length=100)
    temperatura = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    sensacao = models.FloatField()
    umidade = models.IntegerField()
    pressao = models.IntegerField()
    direcao_vento = models.IntegerField()
    velocidade_vento = models.FloatField()

    class Meta:
        app_label = 'data'

    def __str__(self):
        return f"Previsão de {self.cidade} para {self.data_hora_previsao}"