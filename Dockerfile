# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /polls

# Copy the requirements file
COPY requirements.txt /polls/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /polls/

# Expose the port the app runs on
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
