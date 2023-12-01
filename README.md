# HunchaDigitalTask1
A simple backend TODO application using a server-side framework (Django)
- Backend using django framework with SQlLite and CRUD operation
- This project provides a RESTful API for managing tasks using Django and SQLite.

## Prerequisites

To run this application, you will need to have the following installed:

* Python 
* pip install Django after creating virtual environment
* pip install djangorestframework
* SQLite
  
## Installation

1. Clone the repository:
   
   - In terminal of vscode
* command-> git clone <repository_url>

2. Create a virtual environment and activate it:
   - Terminal
* cd <project_directory>
* python3 -m venv venv
* source venv/bin/activate

3. Install the required dependencies:
   - In Terminal
* pip install -r requirements.txt

4. Create the database schema:
   - IN Terminal
* python manage.py makemigrations
* python manage.py migrate

5. Run the development server:
-  IN Terminal
* python manage.py runserver


## The application will be running on http://localhost:8000.

# API Documentation

# Create Task
Endpoint: /create
Method: POST
Request Data:
title: The title of the task (required)
status: The status of the task (optional, defaults to "pending")
Description: Creates a new task.

# Get Task
Endpoint: ' '
Method: GET
Description: Retrieves a specific task with the given ID.

# Update Task
Endpoint: /update/<int:pk>/
Method: PUT
Request Data:
Description: Updates the specified task.

# Delete Task
Endpoint: /delete/<task_id>
Method: DELETE
Description: Deletes the specified task.


