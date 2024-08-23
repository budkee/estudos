from django.db import models
from django.utils import timezone
# ---------- Registro de Usuários ----------
class User(models.Model):
    
    FREQUENCY_CHOICES = [
        ('minutly', 'Minutly'), # A cada minuto para teste
        ('weekly', 'Weekly'),
        ('biweekly', 'Biweekly'),
        ('monthly', 'Monthly'),
        ('semiannual', 'Semiannual'),
    ]
    email = models.EmailField(unique=True)
    frequency = models.CharField(max_length=25, choices=FREQUENCY_CHOICES)

    class Meta:
        app_label = 'newsletter'

    def __str__(self):
        return f"Usuário: {self.email} | Frequência de envios: {self.frequency}"

# ---------- Registro de Envios ----------
class EmailLog(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'newsletter'

    def __str__(self):
        return f"Último envio: {self.timestamp} | Status: {self.status}"
    