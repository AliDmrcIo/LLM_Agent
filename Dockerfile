FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py agent.py tools.py index.html ./

COPY ai/models/ ./ai/models/

EXPOSE 8000

CMD ["python", "main.py"]