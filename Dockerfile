# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
# This is crucial for pydub to work inside the container
RUN apt-get update && apt-get install -y ffmpeg

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your app using uvicorn
# This is what runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]