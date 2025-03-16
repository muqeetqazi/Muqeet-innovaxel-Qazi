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
### Home Page
- **URL**: `http://127.0.0.1:8000/`
- **Features**:
  - List of all URLs with options.
  - Replace <short_code> with actual generated short_code
    

## API Endpoints

1. **Create Short URL**  
   - **Method**: POST  
   - **URL**: `/api/shorten/`  
   - **Request Body**:
     ```json
     {
       "url": "https://www.postman.com/downloads/"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 17,
       "url": "https://tankionline.com/en/",
       "short_code": "QhnViY",
       "created_at": "2025-03-16T15:11:08.732727Z",
       "updated_at": "2025-03-16T15:11:08.732727Z",
       "access_count": 0
     }
     ```



<img width="889" alt="image" src="https://github.com/user-attachments/assets/4f960faa-2467-4768-b22a-73f2ecf4b2fb" />






2. **Retrieve Original URL**  
   - **Method**: GET  
   - **URL**: `/api/shorten/MJxe7s/`  
   - **Response**:
     ```json
     {
       "id": 4,
       "url": "https://www.postman.com/downloads/",
       "short_code": "MJxe7s",
       "created_at": "2025-03-16T11:48:13.639465Z",
       "updated_at": "2025-03-16T11:48:13.639465Z",
       "access_count": 0
     }
     ```

3. **Update Short URL**  
   - **Method**: PUT  
   - **URL**: `/api/shorten/MJxe7s/update/`  
   - **Request Body**:
     ```json
     {
       "url": "https://www.updated-url.com/"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 4,
       "url": "https://www.updated-url.com/",
       "short_code": "MJxe7s",
       "created_at": "2025-03-16T11:48:13.639465Z",
       "updated_at": "2025-03-16T12:00:00.000000Z",
       "access_count": 0
     }
     ```

4. **Delete Short URL**  
   - **Method**: DELETE  
   - **URL**: `/api/shorten/MJxe7s/delete/`  
   - **Response**: `204 No Content`

5. **Get URL Statistics**  
   - **Method**: GET  
   - **URL**: `/api/shorten/<short_code>/stats/`  
   - **Response**:
     ```json
     {
       "id": 4,
       "url": "https://www.postman.com/downloads/",
       "short_code": "MJxe7s",
       "created_at": "2025-03-16T11:48:13.639465Z",
       "updated_at": "2025-03-16T11:48:13.639465Z",
       "access_count": 10
     }
     ```

6. **Redirect to Original URL**  
   - **Method**: GET  
   - **URL**: `/<short_code>/`  
   - **Behavior**: Redirects to the original URL associated with the short code.  
   - **Example**:  
     - Visit `http://127.0.0.1:8000/6ezVSb/` to be redirected to `https://www.postman.com/downloads/`.

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
