FROM python:3.9-slim

# Define arguments that can be used during the build
ARG PIP_UPGRADE

WORKDIR /app

# Install system-level dependencies that are commonly needed
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip if specified
RUN if [ "$PIP_UPGRADE" = "true" ]; then pip install --upgrade pip; fi

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the working directory
COPY . .

# Set up the command to run the FastAPI server
CMD ["uvicorn", "src.deployment.model_container:app", "--host", "0.0.0.0", "--port", "8000"]
