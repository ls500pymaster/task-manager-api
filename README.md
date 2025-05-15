# Task Manager API

A minimal Django project providing a REST API for managing Tasks and Tags.

## Table of Contents

* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Quick Start](#quick-start)
* [Docker](#docker)

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
   git clone git@github.com:ls500pymaster/task-manager-api.git
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
___
## Local Development & Testing
One‑time setup

```bash
poetry install --no-root`
```

#### Run the app

```bash
poetry shell
python manage.py migrate
python manage.py runserver
```

#### Run tests

```bash
pytest -q
```


## Docker

1. Rebuild the image and start container
```bash
docker compose down
docker compose build --no-cache web
docker compose up -d web
```

2. Run tests in container
```bash
python -m pytest -q
```

---
## Contact

Author: Aleksandr
