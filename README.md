
# Cinematic Backend

Bem-vindo ao repositório do backend para o projeto Cinematic! Este backend é responsável por gerenciar a busca e o histórico de filmes usando MongoDB e Flask.

## Índice

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Executando o Projeto](#executando-o-projeto)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Visão Geral

O backend é construído usando o Flask e o PyMongo, e expõe endpoints para buscar filmes e consultar o histórico de buscas. A persistência de dados é realizada no MongoDB.

## Requisitos

- Docker
- Docker Compose
- Python 3.8 ou superior
- MongoDB (via Docker)

## Configuração do Ambiente

### Configuração via Docker

Para configurar e executar o ambiente de desenvolvimento usando Docker e Docker Compose, siga estes passos:

1. **Clone o Repositório**

   ```sh
   git clone https://github.com/seu_usuario/cinematic-backend.git
   cd cinematic-backend
   ```

2. **Configurar Docker e Docker Compose**

   Certifique-se de ter o Docker e Docker Compose instalados. Se não estiverem instalados, siga as instruções na [documentação oficial do Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/).

3. **Construir e Iniciar os Serviços**

   ```sh
   docker-compose up --build
   ```

   Isso irá construir a imagem do backend e iniciar os serviços do MongoDB e do backend Flask.

### Configuração Local

Se preferir executar o backend localmente (fora do Docker), siga estas etapas:

1. **Instalar Dependências**

   Crie um ambiente virtual e instale as dependências:

   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configurar o MongoDB**

   Certifique-se de ter o MongoDB em execução. Se estiver usando Docker, ele será iniciado automaticamente com o `docker-compose up`.

3. **Definir Variáveis de Ambiente**

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

   ```ini
   FLASK_ENV=development
   MONGO_URI=mongodb://localhost:27017/test_database
   ```

## Executando o Projeto

1. **Executar o Backend**

   Com o Docker:

   ```sh
   docker-compose up
   ```

   Localmente:

   ```sh
   flask run
   ```

   O backend estará disponível em `http://localhost:5000`.


## Testes

Para garantir que o backend está funcionando corretamente, você deve executar os testes incluídos no projeto. O projeto utiliza o `unittest` para realizar os testes. Siga as etapas abaixo para rodar os testes:

### Requisitos

Certifique-se de que todos os requisitos do projeto estão instalados. Você pode instalar as dependências necessárias utilizando:

```bash
pip install -r requirements.txt
```

### Executar Testes Unitários

Para rodar os testes unitários, execute o seguinte comando na raiz do projeto:

```bash
python -m unittest discover tests/unit/
```

### Executar Testes de Integração (WIP)

Para rodar os testes de integração, use o comando:

```bash
python -m unittest discover tests/integration/
```
Certifique-se de que os serviços do MongoDB estão em execução antes de rodar os testes.

### Configuração do Ambiente para Testes

Os testes de integração requerem um ambiente de MongoDB em execução. Certifique-se de que o MongoDB está configurado corretamente no Docker ou em outro ambiente antes de executar os testes de integração.

### Observações

- **Testes Unitários:** Esses testes verificam a funcionalidade individual das partes do código, como funções e métodos.
- **Testes de Integração:** Esses testes verificam a integração entre diferentes partes do sistema, incluindo a comunicação com o banco de dados.


## Estrutura do Projeto

- **app.py**: Contém a configuração do Flask e a inicialização do PyMongo.
- **Dockerfile**: Define a imagem Docker para o backend.
- **docker-compose.yml**: Define os serviços Docker para o MongoDB e o backend.
- **requirements.txt**: Lista das dependências Python do projeto.
- **tests/**: Contém os testes de integração para o backend.

## Contribuindo

Se você deseja contribuir para o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commits das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

