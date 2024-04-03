# Django | Python's Back-End Framework

## Projetos versus aplicações

### Qual a diferença entre um projeto e um app? 

Um app é uma aplicação web que executa algo, por exemplo: um sistema de blog, uma base de dados de registros públicos ou uma pequena aplicação de enquete. Um projeto é uma coleção de configurações e apps para um website específico. Um projeto pode conter múltiplos apps. Um app pode estar em múltiplos projetos.

## Estrutura do projeto

    mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

Esses arquivos são:

- O diretório raiz mysite/ é um contêiner para o seu projeto. Seu nome não importa para o Django; você pode renomeá-lo para qualquer nome que você quiser.

- `manage.py`: um utilitário de linha de comando que permite a você interagir com esse projeto Django de várias maneiras. Você pode ler todos os detalhes sobre o manage.py em django-admin and manage.py.
O diretório mysite/ interior é o pacote Python para o seu projeto. Seu nome é o nome do pacote Python que você vai precisar usar para importar coisas do seu interior (por exemplo, mysite.urls).

- `mysite/__init__.py`: um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python. Se você é um iniciante Python, leia mais sobre pacotes na documentação oficial do Python.

- `mysite/settings.py`: configurações para este projeto Django. [Configurações do Django](https://docs.djangoproject.com/pt-br/5.0/topics/settings/) irá revelar para você tudo sobre o funcionamento do settings.

- `mysite/urls.py`: as declarações de URLs para este projeto Django; um “índice” de seu site movido a Django. Você pode ler mais sobre URLs em Despachante de URL.

- `mysite/asgi.py`: um ponto de integração para servidores web compatíveis com ASGI usado para servir seu projeto. Veja [Como fazer o deploy com ASGI](https://docs.djangoproject.com/pt-br/5.0/howto/deployment/asgi/) para mais detalhes.

- `mysite/wsgi.py`: um ponto de integração para servidores web compatíveis com WSGI usado para servir seu projeto. Veja [Como implementar com WSGI](https://docs.djangoproject.com/pt-br/5.0/howto/deployment/wsgi/) para mais detalhes.

## Rodar o servidor localmente
Dentro do diretório contendo o arquivo `manage.py`, rode o seguinte comando:

    $ python manage.py runserver

## Criando aplicações dentro do projeto

    $ python manage.py startapp app

### Estrutura do aplicativo

    app/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

## Views

No framework Django, as views são responsáveis por processar as requisições HTTP e retornar as respostas apropriadas. Elas funcionam como o elo entre os modelos de dados e os templates de visualização, implementando a lógica da aplicação web. As views determinam o que será exibido ao usuário final, controlando o fluxo da aplicação.

### Criando views

Abra o arquivo views.py dentro do aplicativo que você acabou de criar. 
Por exemplo, vamos criar uma classe de view chamada `HomePageView` que renderiza uma página simples de "Hello, Django!" quando acessada:

#### No arquivo `views.py` do seu aplicativo

    from django.http import HttpResponse
    from django.views import View

    class HomePageView(View):
        def get(self, request):
            return HttpResponse("Hello, Django!")

#### No arquivo `urls.py` do seu aplicativo

    from django.urls import path
    from .views import HomePageView

    urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
    ]

### Mapeando a URL para a (classe de) view

> Ao mapear as views no framework Django, estamos definindo **como as URLs da nossa aplicação serão interpretadas e processadas**. Isso envolve associar uma URL a uma função específica (ou **classe**) de view que será responsável por lidar com a requisição correspondente. Este mapeamento é essencial para direcionar corretamente as interações do usuário para as partes apropriadas da aplicação. 

### Adicione a URL do aplicativo ao projeto

Por fim, inclua as URLs do seu aplicativo no arquivo urls.py do projeto principal do Django.

#### No arquivo urls.py do seu projeto principal

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('nome_app.urls')),  # Adicione esta linha
    ]

## Modelos

Ao contrário de Ruby on Rails, por exemplo, as migrações são inteiramente derivada de seu arquivo de modelos, e são essencialmente apenas uma história que o Django pode avançar para atualizar o esquema de banco de dados para coincidir com seus modelos atuais.

Migrações são muito poderosas e permitem que você altere seus modelos ao longo do tempo, à medida que desenvolve o seu projeto, sem a necessidade de remover o seu banco de dados ou tabelas e criar de novo - ele é especializado em atualizar seu banco de dados ao vivo, sem perda de dados. Nós vamos cobri-los com mais profundidade em uma parte posterior do tutorial, mas para agora, lembre-se deste guia de três passos para fazer mudanças nos seus modelos:

Mude seus modelos (em models.py).
Rode python manage.py makemigrations para criar migrações para suas modificações
Rode python manage.py migrate para aplicar suas modificações no banco de dados.
The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.
### Criando modelos
https://docs.djangoproject.com/pt-br/5.0/topics/db/models/
## Links e Referências

- [Documentação](https://docs.djangoproject.com/pt-br/5.0/intro/tutorial01/)