FROM python:3.10-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./django /app

WORKDIR /app

COPY ./entrypoint.sh /

# Executar o app
ENTRYPOINT [ "sh", "/entrypoint.sh" ]