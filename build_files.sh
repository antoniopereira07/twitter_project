#!/bin/bash

# Certifique-se de que o pip está instalado
python3.9 -m ensurepip

# Instalação das Dependências
python3.9 -m pip install -r requirements.txt

# Migrações do Banco de Dados
python3.9 manage.py migrate

# Verifica se o diretório 'staticfiles_build/static' existe e o cria, se necessário
if [ ! -d "/vercel/path0/staticfiles_build/static" ]; then
    mkdir -p /vercel/path0/staticfiles_build/static
fi

# Coleta de Arquivos Estáticos
python3.9 manage.py collectstatic --noinput --clear
