# PetCare - Sistema de Gestão para Petshop

Projeto da matéria **Projeto de Software**, desenvolvido em entregas incrementais (AC1 a AC4).

## Sobre esta entrega (AC1)

Cadastro de Cliente (tutor), com:
- Nome
- Telefone
- E-mail
- Endereço

## Tecnologias

- **Front-end:** HTML + CSS (templates Jinja2)
- **Back-end:** Python + Flask
- **Banco de dados:** MySQL

## Estrutura do projeto

```
ac1_cliente/
├── app.py              # Rotas Flask (back-end)
├── database.py         # Conexão e criação das tabelas no MySQL
├── requirements.txt    # Dependências do projeto
├── setup.bat           # Script para criar o venv e instalar as dependências
├── templates/           # Páginas HTML (front-end)
│   ├── base.html
│   ├── index.html
│   └── clientes.html
└── static/
    └── style.css
```
## Sobre esta entrega (AC2)

Evolução do AC1 (cadastro de cliente), agora com:
- **Edição** dos dados de um cliente já cadastrado
- **Exclusão** de um cliente
- **Pesquisa** de clientes por nome, telefone ou e-mail

## Tecnologias

- **Front-end:** HTML + CSS (templates Jinja2)
- **Back-end:** Python + Flask
- **Banco de dados:** MySQL

## Estrutura do projeto

```
ac2_cliente/
├── app.py                    # Rotas Flask (back-end)
├── database.py                # Conexão e criação das tabelas no MySQL
├── requirements.txt           # Dependências do projeto
├── setup.bat                  # Script de setup para Windows
├── setup.sh                   # Script de setup para Linux/Mac
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── clientes.html          # Lista + pesquisa + cadastro
│   └── editar_cliente.html    # Formulário de edição
└── static/
    └── style.css
```

## Como rodar o projeto

### 1. Pré-requisitos
- Python 3.10+ instalado
- MySQL Server instalado e rodando

### 2. Criar o ambiente virtual e instalar as dependências

**Windows:**
```
setup.bat
```

**Linux/Mac:**
```
./setup.sh
```

### 3. Configurar o banco de dados

Edite as credenciais no início do arquivo `database.py`, se necessário:

```python
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "1234",
    "database": "petcare",
}
```

O banco de dados `petcare` e a tabela `clientes` são criados automaticamente na primeira execução.

### 4. Rodar o programa

**Windows:**
```
python app.py
```

**Linux/Mac:**
```
python3 app.py
```

Acesse no navegador: **http://127.0.0.1:5000**

## Funcionalidades desta entrega

- `/clientes` — lista todos os clientes, com campo de pesquisa
- `/clientes?q=termo` — filtra clientes por nome, telefone ou e-mail
- `/clientes/novo` — cadastra um novo cliente
- `/clientes/<id>/editar` — edita um cliente existente
- `/clientes/<id>/excluir` — remove um cliente

## Próximas entregas (planejadas)

- **AC3:** Cadastro do pet, vinculado ao cliente (AC1/AC2), com pesquisa
- **AC4:** Cadastro de funcionário
