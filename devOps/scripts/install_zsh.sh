#!/bin/bash

# Verifica se o Zsh já está instalado
if ! [ -x "$(command -v zsh)" ]; then
  echo "Instalando Zsh..."
  
  # Instala o Zsh
  sudo apt update
  sudo apt install -y zsh
  
  # Define o Zsh como shell padrão para o usuário atual
  chsh -s $(which zsh)
  
  echo "Zsh instalado com sucesso."
else
  echo "Zsh já está instalado."
fi

