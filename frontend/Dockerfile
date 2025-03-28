FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi jinja2 elasticsearch
EXPOSE 9567
CMD ["sh",  "-c", "fastapi run client.py --port 9567"]
