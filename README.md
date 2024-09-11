# Project Setup and Initialization

This guide outlines the steps to set up and run the project.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Docker
- Flask

## 1. Create and Activate the Virtual Environment

Run the following commands to create and activate a virtual environment:

```bash
# Create the virtual environment
py -3 -m venv .venv

# Activate the virtual environment (Windows)
.venv\Scripts\activate

# Activate the virtual environment (Linux/MacOS)
source .venv/bin/activate
```

## 2. Install Project Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 3. Build and Start Docker Containers

Use Docker Compose to build and start the required containers:

```bash
docker-compose up --build
```

## 4. Access the Docker Bash

Enter the Docker container shell:

```bash
docker-compose exec web bash
```

## 5. Initialize the Database

Set up the database by running the following commands inside the Docker container:

```bash
flask db init
flask db migrate
flask db upgrade
```

## 6. Access the Application

The application will be available at:

[http://localhost:5000/](http://localhost:5000/)

---

You're all set! The application should now be running locally.
