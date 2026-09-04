#!/bin/bash
echo "Criando ambiente virtual (venv)..."
python3 -m venv venv

echo "Ativando o venv e instalando dependencias..."
source venv/bin/activate
pip install -r requirements.txt

echo ""
echo "Pronto! Para rodar o programa, use: source venv/bin/activate  e depois  python3 app.py"
