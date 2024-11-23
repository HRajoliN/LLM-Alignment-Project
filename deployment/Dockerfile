FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.deployment.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
