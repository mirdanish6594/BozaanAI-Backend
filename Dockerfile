# Use a specific, stable Python version
FROM python:3.11.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies, including build tools
# 'build-essential' contains the gcc compiler needed for PyAudio
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg portaudio19-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . .

# Make the start script executable inside the container
RUN chmod +x /app/start.sh

# Set the entrypoint to our new script
ENTRYPOINT ["/app/start.sh"]