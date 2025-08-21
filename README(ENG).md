<h1>News Feed (SIBERS)</h1>

<h3>Stack:</h3>

1. Python
2. Django
3. HTML/CSS
4. PostgreSQL

-----

<h3>Setup Instructions:</h3>

1. Create a PostgreSQL database named ```news_feed_db``` using PgAdmin or the command line.
2. Navigate to the main project folder ```news_project``` and, if needed, create a virtual environment: ```python -m venv venv```
3. Install the required project packages using: ```pip install -r requirements.txt```
4. Create migrations: ```python manage.py makemigrations```
5. Apply the migrations: ```python manage.py migrate```
6. If everything runs successfully, start the project: ```python manage.py runserver```

<h3>Database:</h3>

The project uses PostgreSQL, and for proper functioning, you need to create the database and provide the PostgreSQL username and password. <br>
There are 2 ways to create the database:

1. Using the PgAdmin application
<img align="center" width="1458" height="946" alt="image" src="https://github.com/user-attachments/assets/1b8645b1-81aa-47b6-a14a-1e0077d2adab" />
<img align="center" width="1458" height="945" alt="image" src="https://github.com/user-attachments/assets/beb1bfe6-92ba-43c2-b59d-abd40fdaa758" />

<br>

2. Using the command line <br>
Navigate to the folder where PostgreSQL is installed and launch the console with: ```psql -U postgres``` <br>
Create the database using the command: ```CREATE DATABASE news_feed_db;``` <br>

If your username or password is different, change them in `settings.py` in the fields below: <br>
settings.py
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_feed_db', # DATABASE NAME
        'USER': 'postgres',     # USERNAME
        'PASSWORD': '1234',     # USER PASSWORD
        'HOST': 'localhost',    # LOCAL SERVER ADDRESS
        'PORT': '5432',         # LOCAL SERVER PORT
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
