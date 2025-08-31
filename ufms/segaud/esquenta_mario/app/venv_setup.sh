#! /bin/zsh
# Execute o script com: source venv_setup.sh

# Lista as versões instaladas do Python pelo pyenv
pyenv versions

# Define a versão local do Python para o projeto
pyenv local 3.13

# Mostra a versão do Python em uso (confirmação)
python --version

# Cria um ambiente virtual com a versão selecionada pelo pyenv
python -m venv .venv

# Ativa o ambiente virtual
source .venv/bin/activate

# Atualiza o pip e lista pacotes
python -m ensurepip --upgrade
pip install --upgrade pip
pip list

# Para sair do ambiente virtual, use:
# deactivate

# Para remover e recriar o ambiente:
# rm -rf .venv && python -m venv .venv
