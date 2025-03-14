FROM python:3.11-slim

WORKDIR /app

COPY . .

CMD ["python", "./examples/factory_pattern/factory_example.py"]
