# Desenvolvimento de um CRUD com Python e biblioteca Streamlit

## Pré-requisitos

- Docker
- Docker Compose

## Configuração

1. Clone o repositório para o seu ambiente local:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie um arquivo `.env` na raiz do projeto e adicione a variável de ambiente `MONGO_URI`:
   ```env
   MONGO_URI=mongodb://mongo:27017
   ```

3. Certifique-se de que o arquivo `docker-compose.yml` está configurado corretamente:
   ```yaml
   version: "3.8"

   services:
     web:
       build: .
       ports:
         - "5000:5000"
       depends_on:
         - mongo
       environment:
         - MONGO_URI=mongodb://mongo:27017

     mongo:
       image: mongo:latest
       ports:
         - "27017:27017"
       volumes:
         - mongo-data:/data/db

   volumes:
     mongo-data:
   ```

4. Certifique-se de que o arquivo `Dockerfile` está configurado corretamente:
   ```Dockerfile
   FROM python:3.10-slim

   WORKDIR /app

   COPY requirements.txt .

   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 5000

   CMD ["python", "run.py"]
   ```

## Executando a aplicação

1. Inicie os serviços Docker:
   ```sh
   docker-compose up --build
   ```

2. Verifique os logs do serviço web para garantir que a aplicação está rodando corretamente:
   ```sh
   docker-compose logs -f web
   ```

3. Acesse a aplicação no navegador:
   ```sh
   http://localhost:5000
   ```

## Estrutura do Projeto

- `app/`: Contém os arquivos da aplicação Flask.
  - `templates/`: Contém os arquivos HTML.
  - `static/`: Contém os arquivos CSS e JS.
- `Controllers/`: Contém os controladores da aplicação.
- `models/`: Contém os modelos de dados da aplicação.
- `services/`: Contém os serviços da aplicação, como a conexão com o banco de dados.
- `requirements.txt`: Lista de dependências do projeto.
- `Dockerfile`: Arquivo de configuração do Docker para a aplicação.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose para a aplicação.

## Debugging

1. Para verificar os prints de debug, você pode acessar os logs do serviço web:
   ```sh
   docker-compose logs -f web
   ```

2. Realize ações na aplicação (como login e cadastro) e observe os logs no terminal para ver os prints que foram adicionados.

## Parando a aplicação

1. Para parar os serviços Docker, execute:
   ```sh
   docker-compose down
   ```

2. Para remover os volumes Docker, execute:
   ```sh
   docker-compose down -v
   ```