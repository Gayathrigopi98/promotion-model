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

ENTRYPOINT ["streamlit", "run", "webview.py", "--server.port=81", "--server.address=0.0.0.0"]
