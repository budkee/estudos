FROM python:3.10-alpine

WORKDIR /app

COPY ./app .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# COPY ./requirements.txt .
# COPY ./entrypoint.sh .

ENTRYPOINT [ "sh", "./entrypoint.sh" ]