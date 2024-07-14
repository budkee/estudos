from rest_framework import serializers
from .models import User, EmailLog

class UserSerializer(serializers.ModelSerializer):
    
    # last_email_sent = serializers.SerializerMethodField()

    # def get_last_email_sent(self, obj):
    #     # Aqui você pode implementar a lógica para obter a data do último e-mail enviado para o usuário obj
    #     # Por exemplo, pode ser algo como:
    #     last_log = EmailLog.objects.filter(user=obj).order_by('-timestamp').first()
    #     if last_log:
    #         return last_log.timestamp
    #     return None

    class Meta:
        model = User
        fields = ['id', 'email', 'frequency']

class EmailLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmailLog
        fields = ['timestamp', 'status']