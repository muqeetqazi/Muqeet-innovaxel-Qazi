# Muqeet-innovaxel-Qazi

## Overview
This is a URL Shortening Service implemented in Python Django using SQL (MySQL). It provides a RESTful API to create, retrieve, update, and delete short URLs, along with access statistics.

## Features
- Create a short URL from a long URL
- Retrieve the original URL using the short code
- Update an existing short URL
- Delete a short URL
- Get access statistics for a short URL

## Project Structure
```
.
├── manage.py
├── requirements.txt
├── url_shortener/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shortener/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
└── README.md
```

## Prerequisites
- Python 3.x
- Django
- MySQL
- Django REST Framework

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/muqeetqazi/Muqeet-innovaxel-Qazi.git
cd Muqeet-innovaxel-Qazi
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure MySQL database in `shortener/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'url_shortener',
        'USER': 'root',
        'PASSWORD': 'Qazi@12321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Create Short URL
```
POST /api/shorten/
{
//will later
    
}
```

### Get Original URL
```
//will later
```

### Update Short URL
```
PUT /api/url/{short_code}/
{
  //will later
}
```

### Delete Short URL
```
//will later
```

### Get URL Statistics
```
//will later
```

## Running Tests
```bash
python manage.py test
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details. 
