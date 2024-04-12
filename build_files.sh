#!/bin/bash

# Certifique-se de que o pip está instalado
python3.9 -m ensurepip

# Criação e ativação do ambiente virtual
python3.9 -m venv myenv
source myenv/bin/activate

# Instalação das Dependências
python3.9 -m pip install -r requirements.txt

# Migrações do Banco de Dados
python3.9 manage.py migrate

# Verifica se o diretório 'static' existe e o cria, se necessário
if [ ! -d "/vercel/path0/static" ]; then
    mkdir -p /vercel/path0/static
fi

# Coleta de Arquivos Estáticos
python3.9 manage.py collectstatic --noinput --clear
