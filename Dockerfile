# Start with an official Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose port 81 for the application
EXPOSE 81

ENTRYPOINT ["uvicorn" , "model_app:app" ,"--host" ,"0.0.0.0", "--port", "81"]
