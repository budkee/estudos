import os
import json
# -------- Django Framework -----------------
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# -------- REST Framework -----------------
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
# -------- Newsletter App -----------------
from .models import User
from .serializers import UserSerializer
from .services import UserService, DataService
from .forms import EmailForm

# ----------------- Visões -----------------------


class UserViewSet(viewsets.ViewSet):

    permission_classes = [permissions.AllowAny]
    user_service = UserService()
    
    # ---------- Listar todos os usuários registrados --------------
    @action(detail=True, methods=['get'], url_path='recupera_usuarios')
    def recupera_usuarios(self, request):

        if request.method == 'GET':
            
            queryset = self.user_service.pegar_todos_usuarios()
            serializer = UserSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    # ---------- Registrar um novo usuário --------------
    @action(detail=False, methods=['post'], url_path='cadastrar_usuario')
    def cadastrar_usuario(self, request):
        
        if request.method == 'POST':
            
            email = request.data.get('email')
            frequency = request.data.get('frequency')
        
            if not email or not frequency:
                return Response({"error": "Email and frequency are required"}, status=status.HTTP_400_BAD_REQUEST)
        
            user = self.user_service.inserir_usuario(email, frequency)
            serializer = UserSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # ---------- Descadastrar um usuário --------------
    @action(detail=False, methods=['post'], url_path='descadastrar_usuario')
    def descadastrar_usuario(self, request):
        
        if request.method == 'DELETE':
            
            email = request.data.get('email')
        
            if not email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                success = self.user_service.remover_usuario(email)
            
                if success:
                    return Response({"message": "Usuário descadastrado com sucesso!"}, status=status.HTTP_200_OK)
                else:   
                    return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
                
            except Exception as e:
                return Response({"error": f"Erro ao descadastrar usuário: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class DataViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post', 'get'], url_name='enviar_email')
    def enviar_email(self, request):

        if request.method == 'POST':
            form = EmailForm(request.POST)
            
            if form.is_valid():
            
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipient = form.cleaned_data['recipient']
            
                send_mail(subject, message, os.getenv('DEFAULT_FROM_EMAIL'), [recipient])
                return Response({'message': 'Email enviado com sucesso!'})
        else:
            form = EmailForm()
        return render(request, 'index.html', {'form': form})


    
#     
#     data_service = DataService()

#     # ---------- Enviar notificações aos usuários cadastrados --------------
#     @action(detail=False, methods=['post'], url_path='send_notifications')
#     # @api_view(['POST'])
#     def enviar_boletim(self, request):

#         self.data_service.enviar_boletim()
        
#         return Response({"message": "Notifications sent successfully"}, status=status.HTTP_200_OK)
