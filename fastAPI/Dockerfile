FROM python:3.13-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY /app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
