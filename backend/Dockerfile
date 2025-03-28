FROM python:3.13-slim
WORKDIR /api
RUN pip install --no-cache-dir "fastapi[standard]" uvicorn elasticsearch
COPY . .
ENV ELASTICSEARCH_HOST=http://elasticsearch:9200
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "9567"]
