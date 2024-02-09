#

## Criar um serviço de mensageria utilizando Docker e Python pode ser uma ótima maneira de distribuí-lo para outras máquinas. 

### Aqui estão alguns passos para te ajudar a configurar isso:

1. Crie uma pasta para o projeto do serviço de mensageria.
   ```bash
   mkdir servico_mensageria
   cd servico_mensageria
   ```

2. Crie um arquivo chamado `Dockerfile` (sem extensão).
   ```bash
   touch Dockerfile
   ```

3. Abra o arquivo `Dockerfile` e adicione o seguinte conteúdo:
   ```Dockerfile
   FROM python:3.9

   # Configuração do diretório de trabalho
   WORKDIR /app

   # Copia o arquivo requirements.txt para o container
   COPY requirements.txt .

   # Instala as dependências do projeto
   RUN pip install --no-cache-dir -r requirements.txt

   # Copia todos os arquivos do projeto para o container
   COPY . /app

   # Define o comando inicial do container
   CMD ["python", "app.py"]
   ```

4. Crie um arquivo chamado `app.py`.
   ```bash
   touch app.py
   ```

5. Abra o arquivo `app.py` e adicione o código do serviço de mensageria em Python que deseja distribuir. Por exemplo:
   ```python
   # Importe as bibliotecas necessárias
   from flask import Flask

   # Configure o aplicativo Flask
   app = Flask(__name__)

   # Defina as rotas e ações da sua aplicação

   @app.route('/')
   def hello_world():
       return 'Olá, mundo!'
   
   # Execute o aplicativo Flask
   if __name__ == '__main__':
       app.run()
   ```

6. Crie um arquivo chamado `requirements.txt` e adicione as dependências do seu projeto. Por exemplo:
   ```
   flask==1.1.2
   ```

7. Agora você está pronto para criar a imagem Docker do seu serviço de mensageria. No diretório `servico_mensageria`, execute o seguinte comando:
   ```bash
   docker build -t servico_mensageria .
   ```

8. Depois de construir a imagem, você pode executar o serviço de mensageria em um contêiner Docker usando o seguinte comando:
   ```bash
   docker run -p 5000:5000 servico_mensageria
   ```

   Isso mapeará a porta 5000 de dentro do contêiner para a porta 5000 do host, permitindo que você acesse o serviço de mensageria em `http://localhost:5000`.

9. Agora você pode distribuir o serviço de mensageria em um contêiner Docker para outras máquinas, bastando enviar a imagem Docker (criada no passo 7) para as outras máquinas e executar o comando `docker run` nelas.

   Certifique-se de que as outras máquinas tenham o Docker instalado e a execução de contêineres Docker esteja permitida.

Espero que isso tenha te ajudado a criar um serviço de mensageria utilizando Docker e Python!