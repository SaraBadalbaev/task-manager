# Tasks Manager App #

The Tasks Manager App is a task management system developed using FastAPI for the backend and JavaScript for the frontend. This application enables users to create, read, and delete tasks efficiently. Tasks can be filtered by labels and priority levels, which include high, medium, and low. The backend, built with Python and FastAPI, integrates with Firebase for data storage, ensuring robust and scalable handling of task data. The frontend, developed using JavaScript, offers a user-friendly interface for seamless task management.

## Features

1. **Create Task:** Users can create a new task by providing a title, description, label, priority, and status.
2. **Display Tasks:** Existing tasks are displayed, showing their title, description, priority, lebel and status.
3. **Delete Task:** Users can delete a task.
4. **Filter By Priority:** Users can filter tasks according to their priority (high, medium, low).
5. **Filter By Lebal:** Users can filter tasks according to their label

## Technology Stack:

**FastAPI**: A modern, fast web framework for building APIs with Python.

**Firebase**: A platform developed by Google for creating mobile and web applications that offers a real-time database, authentication, and various other services.

## Prerequisites

* Docker
* Docker Compose

## Installation 

1. Clone this repository to your local machine:
```
git clone (https://github.com/SaraBadalbaev/task-manager.git)
```
2. Build the Docker images and run the containers using docker-compose:
```
docker-compose up --build
```
The backend of the application is now running at: http://localhost:8080
