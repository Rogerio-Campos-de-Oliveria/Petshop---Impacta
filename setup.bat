@echo off
echo Criando ambiente virtual (venv)...
python -m venv venv

echo Ativando o venv e instalando dependencias...
call venv\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Pronto! Para rodar o programa, use: venv\Scripts\activate.bat  e depois  python app.py
pause
