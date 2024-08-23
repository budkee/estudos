from django.contrib import admin
from .models import EmailLog, User

admin.site.register(User)
admin.site.register(EmailLog)