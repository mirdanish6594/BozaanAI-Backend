# Use a stable, recent Python version like 3.11, which has good package support
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies in a single, clean layer.
# This is a best practice to ensure apt cache is updated right before install.
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg portaudio19-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]