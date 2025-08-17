# Use a stable, recent Python version
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies, including build tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg portaudio19-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Expose the port (Hugging Face uses 7860 by default for Gradio/FastAPI)
EXPOSE 7860

# The command to start the app
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]