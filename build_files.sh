#!/bin/bash

# Instalação das Dependências
python3.9 -m pip install -r requirements.txt

# Migrações do Banco de Dados
python3.9 manage.py migrate

# Coleta de Arquivos Estáticos
python3.9 manage.py collectstatic --noinput --clear
