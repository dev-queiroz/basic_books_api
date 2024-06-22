# Books API with FastAPI and SQLite

Este projeto demonstra uma API RESTful para gerenciar uma coleção de livros, construída usando o FastAPI (um framework web de alto desempenho para Python) e o SQLite (um banco de dados relacional leve). Ele permite que você:

- Liste todos os livros no banco de dados.
- Recupere um livro específico pelo seu ID.
- Adicione novos livros ao banco de dados (por meio de entrada no console para este exemplo).

## Começando

### Pré-requisitos:

- Python 3.6 ou posterior
- pip (instalador de pacotes Python)

### Instalação:

Clone este repositório e instale as dependências necessárias:

```bash
git clone https://github.com/your-username/books-api.git
cd books-api
pip install fastapi databases uvicorn
```

# Configuração do Banco de Dados:

Execute o script create_db.py para criar o banco de dados SQLite books.db:

```bash
python create_db.py
```

# Executando a API:

Inicie o servidor da API para os endpoints de listagem e recuperação de livros:

```bash
uvicorn main_api:app --host 127.0.0.1 --port 8000
```

# Endpoints da API

- “GET /”: Retorna uma mensagem de boas-vindas.
- “GET /books/”: Lista todos os livros no banco de dados.
- “GET /books/{book_id}”: Recupera um livro específico pelo seu ID (substitua “{book_id}” pelo ID real).

# Adicionando Livros

### Implementação Atual:

Embora o código fornecido inclua um script “add_books.py” para adicionar livros por meio de entrada no console, ele não está diretamente integrado à aplicação FastAPI.

### Via chamadas de API:

- Modifique o “add_books.py” para usar o FastAPI para lidar com requisições/respostas HTTP.
- Crie um novo endpoint em “main_api.py” para receber dados do livro (título, autor) no corpo da requisição.

Essa abordagem aprimorada permitiria adicionar livros por meio de chamadas de API.

Exemplo de Uso:

```bash
curl http://127.0.0.1:8000/books/
```

# Contribuindo

Serão aceitas contribuições para este projeto através de pull requests!
