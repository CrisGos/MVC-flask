

# Use an official Python runtime as a image
FROM python:3.12.0

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Copy .env file
COPY .env .env

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_ENV=development

# Run the application
CMD ["python", "manage.py", "runserver", "--host=0.0.0.0"]