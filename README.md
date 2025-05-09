# API Django - Cadastro de Usuários

Este projeto é uma API desenvolvida em Django para realizar operações de CRUD (Create, Read, Update, Delete) em um cadastro simples de usuários.

## Funcionalidades

- Criar usuários
- Listar todos os usuários
- Buscar usuário por ID
- Atualizar dados do usuário
- Deletar usuário

Cada usuário possui os seguintes campos:
- ID (gerado automaticamente)
- Nome
- E-mail
- Idade

## Tecnologias utilizadas

- Python 3.11+
- Django 5.x
- SQLite (como banco de dados)

## Como rodar o projeto localmente

1. Clone o repositório:

   git clone https://github.com/taiiisoares/django-api.git
   cd django-api

2. Crie e ative o ambiente virtual:

   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate (Linux/Mac)

3. Instale as dependências:

   pip install -r requirements.txt

4. Aplique as migrações:

   python manage.py migrate

5. Rode o servidor local:

   python manage.py runserver

6. Acesse no navegador:

   http://127.0.0.1:8000/

## Estrutura básica

- api_root/ - Diretório do projeto Django
- usuarios/ - Aplicação principal da API
- manage.py - Arquivo principal de execução

## Endpoints

- GET /usuarios/ - Lista todos os usuários
- POST /usuarios/ - Cria um novo usuário
- GET /usuarios/<id>/ - Retorna um usuário específico
- PUT /usuarios/<id>/ - Atualiza um usuário específico
- DELETE /usuarios/<id>/ - Deleta um usuário específico

---

Desenvolvido com 💻 por Tainá.
