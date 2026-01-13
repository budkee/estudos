#!/bin/bash

echo "⚠️ Resetando ambiente..."
docker compose down -v
docker compose up -d --build
