FROM python:3.8-slim

WORKDIR /app

# Copy only production requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . .

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "src.deployment.fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]
