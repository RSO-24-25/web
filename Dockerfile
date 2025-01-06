# Base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8501

# Command to run your application
CMD ["streamlit", "run", "app.py", "--server.port", "8501"] 
