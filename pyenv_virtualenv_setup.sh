#! /bin/zsh
# Execute este script com: source pyenv_virtualenv_setup.sh
# Ele criará e ativará um ambiente virtual integrado ao pyenv.

# Nome do virtualenv (pode ser alterado)
VENV_NAME="meu-projeto"
PYTHON_VERSION="3.13.0"

# Mostra versões do Python disponíveis
echo ">>> Versões do Python disponíveis no pyenv:"
pyenv versions

# Define a versão do Python para o projeto (instale antes com pyenv install)
echo ">>> Definindo versão local do Python para $PYTHON_VERSION"
pyenv local $PYTHON_VERSION

# Cria o virtualenv se não existir
if ! pyenv versions --bare | grep -q "^$VENV_NAME$"; then
    echo ">>> Criando virtualenv $VENV_NAME com Python $PYTHON_VERSION"
    pyenv virtualenv $PYTHON_VERSION $VENV_NAME
else
    echo ">>> Virtualenv $VENV_NAME já existe"
fi

# Ativa o ambiente virtual
echo ">>> Ativando o virtualenv $VENV_NAME"
pyenv activate $VENV_NAME

# Atualiza pip
echo ">>> Atualizando pip..."
pip install --upgrade pip

# Lista pacotes instalados
echo ">>> Pacotes instalados:"
pip list

# Para desativar, use:
# pyenv deactivate

# Para remover o virtualenv, use:
# pyenv virtualenv-delete $VENV_NAME
