# HunchaDigitalTask1
A simple backend application using a server-side framework (Django)
- Backend using django framework with SQlLite.
- This project provides a RESTful API for managing tasks using Django and SQLite.

## Prerequisites

To run this application, you will need to have the following installed:

* Python 
* Django 
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
   -  Terminal
* pip install -r requirements.txt

4. Create the database schema:
   - Terminal
* python manage.py makemigrations
* python manage.py migrate






## The application will be running on http://localhost:8000.

# API Documentation
Task List
Endpoint: /tasks
Method: GET
Description: Retrieves a list of all tasks.
Create Task
Endpoint: /tasks
Method: POST
Request Data:
title: The title of the task (required)
status: The status of the task (optional, defaults to "pending")
Description: Creates a new task.
Get Task
Endpoint: /tasks/<task_id>
Method: GET
Description: Retrieves a specific task with the given ID.
Update Task
Endpoint: /tasks/<task_id>
Method: PUT
Request Data:
title: The updated title of the task (required)
status: The updated status of the task (optional)
Description: Updates the specified task.
Delete Task
Endpoint: /tasks/<task_id>
Method: DELETE
Description: Deletes the specified task.


