FROM python:3.9-slim

WORKDIR /app

RUN pip install redis psycopg2-binary

COPY worker.py .

CMD ["python", "worker.py"]
