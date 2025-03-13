# Snippets | Django

## Sumário

- [Parte Teórica](#teórica)
- [Parte Prática](#prática)

## Teórica

- [Documentação](https://docs.djangoproject.com/en/4.2/)
- [Documentação do suporte ao fuso horário](https://docs.djangoproject.com/pt-br/4.0/topics/i18n/timezones/)

Um projeto de desenvolvimento de um aplicativo envolveria atividades como análise de requisitos, design, programação, testes e implantação do aplicativo.

## Prática

### Como alterar seus modelos no banco de dados?

1. Mude seus modelos em models.py
2. Rode python manage.py makemigrations para criar migrações para suas modificações
3. Rode python manage.py migrate para aplicar suas modificações no banco de dados

- [Documentação do django-admin](https://docs.djangoproject.com/pt-br/4.0/ref/django-admin/) para saber mais sobre o utilitário manage.py