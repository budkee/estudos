"""
    Serviços:
    1. Cadastro e descadastro de usuário.
    2. Envio de e-mails aos usuários cadastrados.

"""
import os
import pytz
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
# from email.mime.text import MIMEText 
from data.models import Previsao  
from .models import User, EmailLog
from data.serializers import PrevisaoSerializer

# ------------ Registro de Usuários ------------
class UserService:
    
    def inserir_usuario(self, email, frequency):
        user, created = User.objects.using('db_newsletter').get_or_create(email=email, defaults={'frequency': frequency})
        if not created:
            user.frequency = frequency
            user.save(using='db_newsletter')
        return user

    def remover_usuario(self, email):
        try:
            user = User.objects.using('db_newsletter').get(email=email)
            user.delete(using='db_newsletter')
            return True
        except User.DoesNotExist:
            return False

    def pegar_todos_usuarios(self):
        return User.objects.using('db_newsletter').all()

# ------------ Envio e Registro de Boletins ------------
class DataService:
    
    def __init__(self):
        self.timezone = pytz.timezone(os.getenv('TZ', 'America/Campo_Grande'))

    def calculate_start_date(self, frequency):
        current_date = datetime.now(self.timezone)
        if frequency == 'minutely':
            return current_date - timedelta(minutes=1)
        elif frequency == 'weekly':
            return current_date - timedelta(days=7)
        elif frequency == 'biweekly':
            return current_date - timedelta(days=15)
        elif frequency == 'monthly':
            return current_date - timedelta(days=30)
        elif frequency == 'semiannual':
            return current_date - timedelta(days=182)
        else:
            return current_date - timedelta(days=7)  # Default to weekly if frequency is not recognized

    def get_weather_data_by_period(self, start_date, end_date):
        return Previsao.objects.using('db_data').filter(data_hora_previsao__range=(start_date, end_date))

    def enviar_boletim_personalizado(self):
        users = User.objects.using('db_newsletter').all()
        for user in users:
            start_date = self.calculate_start_date(user.frequency)
            end_date = datetime.now(self.timezone)
            weather_data = self.get_weather_data_by_period(start_date, end_date)
            success = self.send_email(user.email, weather_data)
            if success:
                EmailLog.objects.create(user=user, status='SUCCESS')
            else:
                EmailLog.objects.create(user=user, status='FAILED')

    def send_email(self, to_email, weather_data):
        serializer = PrevisaoSerializer(weather_data, many=True)
        subject = "Weather Report"
        body = f"Here is your weather report:\n\n{serializer.data}"

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [to_email],
                fail_silently=False,
            )
            return True
        except Exception as e:
            print(f"Failed to send email to {to_email}: {str(e)}")
            return False