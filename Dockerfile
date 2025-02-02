# Use official Python image from Docker Hub
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose port 8000 (default port for Django development server)
EXPOSE 8000

# Run Django app using the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
