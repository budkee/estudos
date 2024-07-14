from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # ------ Django Admin ----------
    path('admin/', admin.site.urls),
    # ------ Django REST ----------
    path('api-auth/', include('rest_framework.urls')),
    # ------ UI Data ----------
    # ------ Swagger Doc ----------
    # ------ Data API ----------
    path('api/data/', include('data.urls')),
    # ------ Newsletter API ----------
    path('api/newsletter/', include('newsletter.urls')),
]
