from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, DataViewSet

router = routers.DefaultRouter()
router.register(r'newsletter', UserViewSet, basename='newsletter')
router.register(r'data', DataViewSet, basename='data')

urlpatterns = [
    path('', UserViewSet.as_view({
        'get': 'recupera_usuarios'
    }), name='recupera_usuarios'),
    path('cadastrar_usuario', UserViewSet.as_view({
        'post': 'cadastrar_usuario'
    }), name='cadastrar_usuario'),
    path('descadastrar_usuario', UserViewSet.as_view({
        'delete': 'descadastrar_usuario'
    }), name='descadastrar_usuario'),
    path('enviar_email', DataViewSet.as_view({
        'post': 'enviar_email',
        'get': 'enviar_email'
    }), name='enviar_email')

]
