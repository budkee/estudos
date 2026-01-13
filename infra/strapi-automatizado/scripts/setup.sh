#!/bin/bash

echo "🔧 Configurando ambiente..."

cp .env.example .env

docker compose pull
docker compose build

echo "✅ Ambiente configurado com sucesso"