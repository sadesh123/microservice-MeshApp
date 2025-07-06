# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

# Expose the port (adjust based on service)
EXPOSE 5002  

# Run the app
CMD ["python", "app.py"]
