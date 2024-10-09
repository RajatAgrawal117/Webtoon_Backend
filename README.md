
# Webtoon Management API

## Overview

This project is a Django-based RESTful API designed to manage a collection of webtoons, inspired by popular webtoon content. It allows users to fetch, add, and delete webtoon entries with details such as titles, descriptions, and characters.

## Features

- **Fetch all webtoons**: Retrieve a list of all webtoons with basic information.
- **Add new webtoon**: Create a new webtoon entry with details.
- **Fetch specific webtoon**: Retrieve detailed information about a specific webtoon by its ID.
- **Delete webtoon**: Remove a webtoon entry by its ID.
- **Secure API**: Implements JWT-based authentication for secure access to certain endpoints.

## Technologies Used

- **Django**: Web framework for building the API.
- **Django REST Framework**: Toolkit for building Web APIs.
- **PostgreSQL/MongoDB**: Database to store webtoon data (specify which one you used).
- **JWT**: For authentication.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Database (PostgreSQL/MongoDB)

### Steps

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Create a database in PostgreSQL or MongoDB and update the settings in `settings.py`.

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server:**

   ```bash
   python manage.py runserver
   ```

   Your API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **GET /api/webtoons/**: Fetch all webtoons
- **POST /api/webtoons/**: Add a new webtoon
- **GET /api/webtoons/{id}/**: Fetch a specific webtoon by ID
- **DELETE /api/webtoons/{id}/**: Delete a webtoon by ID

## Authentication

For secure endpoints (POST and DELETE), you will need to include a JWT token in the request headers:

```http
Authorization: Token <your_jwt_token>
```

## Testing

To run tests, use the following command:

```bash
python manage.py test
```

```
