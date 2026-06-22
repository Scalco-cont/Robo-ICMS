FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Criar diretórios persistentes
RUN mkdir -p src/downloads src/database

EXPOSE 3939

# Gunicorn com 4 workers + 2 threads cada = 8 requisicoes simultaneas
# --preload: elimina cold start carregando o app antes dos workers subirem
# gthread: worker que suporta threads, ideal para processamento de arquivos
CMD ["gunicorn", "--bind", "0.0.0.0:3939", "--workers", "4", "--worker-class", "gthread", "--threads", "2", "--timeout", "120", "--preload", "src.main:app"]
