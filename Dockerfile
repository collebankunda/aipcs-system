
# Base image for FastAPI app
FROM python:3.10

WORKDIR /app
COPY server/ /app/server/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
