FROM python:3.10-alpine3.20

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

COPY ./scripts/entrypoint.sh ./scripts/entrypoint.sh

COPY ./scripts/wait-for-it.sh ./scripts/wait-for-it.sh

# EXPOSE 5001 - já tem no compose

RUN chmod +x ./scripts/wait-for-it.sh

CMD [ "./scripts/wait-for-it.sh", "${POSTGRES_DB}:${POSTGRES_PORT}", "--", "host=${POSTGRES_HOST}" ]

ENTRYPOINT [ "sh", "./scripts/entrypoint.sh" ]