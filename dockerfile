# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY backend/ .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend files
COPY frontend/ /app/frontend/

# Expose the application port
EXPOSE 8000

# Run the backend server
CMD ["uvicorn", "integration_module:app", "--host", "0.0.0.0", "--port", "8000"]
