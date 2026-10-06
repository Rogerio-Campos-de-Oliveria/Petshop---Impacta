# PetCare - Sistema de Gestão para Petshop

Projeto da matéria **Projeto de Software**, desenvolvido em entregas incrementais (AC1 a AC4). Este repositório reúne o resultado final, com tudo que foi desenvolvido em cada entrega.

## O que cada entrega adicionou

| Entrega | O que foi adicionado |
|---|---|
| **AC1** | Cadastro de Cliente (tutor): nome, telefone, e-mail e endereço |
| **AC2** | Edição, exclusão e pesquisa de clientes (por nome, telefone ou e-mail) |
| **AC3** | Cadastro de Pet, vinculado a um cliente, com edição, exclusão e pesquisa (por nome, espécie ou tutor) |
| **AC4** | Cadastro de Funcionário do petshop |

## Tecnologias

- **Front-end:** HTML + CSS (templates Jinja2)
- **Back-end:** Python + Flask
- **Banco de dados:** MySQL

## Estrutura do projeto

```
petshop_completo/
├── app.py                     # Rotas Flask (back-end)
├── database.py                # Conexão e criação das tabelas no MySQL
├── requirements.txt           # Dependências do projeto
├── setup.bat                  # Script de setup para Windows
├── setup.sh                   # Script de setup para Linux/Mac
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── clientes.html          # Cadastro + pesquisa de clientes (AC1/AC2)
│   ├── editar_cliente.html    # Edição de cliente (AC2)
│   ├── pets.html              # Cadastro + pesquisa de pets (AC3)
│   ├── editar_pet.html        # Edição de pet (AC3)
│   └── funcionarios.html      # Cadastro de funcionários (AC4)
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

> No Linux, o MySQL costuma bloquear login do `root` por senha. Nesse caso, crie um
> usuário próprio (ex: `petcare`) e defina a variável de ambiente `DB_USER` antes
> de rodar o programa.

O banco de dados `petcare` e as tabelas `clientes`, `pets` e `funcionarios` são criadas automaticamente na primeira execução.

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

## Rotas da aplicação

**Cliente (AC1/AC2):**
- `/clientes` — lista com pesquisa (`?q=termo`)
- `/clientes/novo` — cadastra
- `/clientes/<id>/editar` — edita
- `/clientes/<id>/excluir` — exclui

**Pet (AC3):**
- `/pets` — lista com pesquisa (`?q=termo`)
- `/pets/novo` — cadastra, vinculado a um cliente
- `/pets/<id>/editar` — edita
- `/pets/<id>/excluir` — exclui

**Funcionário (AC4):**
- `/funcionarios` — lista
- `/funcionarios/novo` — cadastra



