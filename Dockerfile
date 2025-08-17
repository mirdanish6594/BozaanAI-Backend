# Use a specific, stable Python version
FROM python:3.11.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg portaudio19-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Use ENTRYPOINT to make the container run like an executable.
# This is more robust than CMD and less likely to be overridden.
ENTRYPOINT ["/usr/local/bin/python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]