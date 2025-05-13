# Task Manager API

A minimal Django project providing a REST API for managing Tasks and Tags.

## Table of Contents

* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Quick Start](#quick-start)

---

## Overview

This project offers a REST API to:

* Perform CRUD operations on Tasks
* Perform CRUD operations on Tags
* Associate multiple Tags with a Task and vice versa
* Filter Tasks by status and tags
* Secure the API using HTTP Basic Authentication

---

## Tech Stack

* Python 3.11
* Django 4.x
* Django REST Framework
* django-filter
* SQLite (default for local development)
* Poetry for dependency management
* Docker & Docker Compose (lightweight development setup)

---

## Quick Start

1. Clone the repository:

   ```bash
   git clone ...
   cd task-manager-api
   ```

2. Install dependencies with Poetry:

   ```bash
   poetry install --no-root
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

---
## Contact

Author: Aleksandr
