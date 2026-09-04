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

## Como rodar o projeto

### 1. Pré-requisitos
- Python 3.10+ instalado
- MySQL Server instalado e rodando

## Próximas entregas (planejadas)

- **AC2:** Edição, exclusão e pesquisa do cliente
- **AC3:** Cadastro do pet, vinculado ao cliente (AC1), com pesquisa
- **AC4:** Cadastro de funcionário
