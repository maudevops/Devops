# Use an official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first to cache layer
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask app source code into the container
COPY src/ ./src/

# Set environment variables (optional)
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Expose port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]

