# Usa uma imagem base do Python
FROM python:3.8-slim-buster

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o conteúdo do projeto para o diretório de trabalho
COPY . .

# Define o comando padrão para executar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

