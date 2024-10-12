# Django Project Setup

This guide explains how to build and run the Django application using a virtual environment (`venv`) and Docker.

## Prerequisites

- Python 3.x
- Docker
- Git

## 1. Setup using Virtual Environment (`venv`)

### Step 1: Clone the Repository

First, clone the repository:

```bash
git clone https://github.com/Sebaks1/CapstoneDjango1.git
cd your-repo-directory

# Create a virtual environment
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate


# Install pip
# Create requirements.txt
pip install -r requirements.txt

# Run the Django application to check if the installagions were successful
python manage.py migrate
python manage.py runserver

# The application should run on http://127.0.0.1:8000/. if the installations 
# are successful

# Setup Docker