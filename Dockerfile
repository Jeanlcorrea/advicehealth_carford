# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY . .

# Defina a variável de ambiente para que o Flask seja executado no modo de produção
ENV FLASK_ENV=production
ENV FLASK_APP=app:create_app

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Defina o comando para executar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
