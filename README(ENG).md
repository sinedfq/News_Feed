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

```
------

If you need to change the design of your web application, use the ```<styles>``` field in your HTML markup

-----

<h3>Usage Instructions:</h3>
When you follow the link, you will be taken to the main page where all created news items are displayed

<img width="1919" height="917" alt="image" src="https://github.com/user-attachments/assets/24583166-81a3-4321-af7f-431912142286" />
*some images are not displayed because they have been deleted

To create a new news item, click on the "Add News" button in the top left corner of the screen. After clicking, you will be taken to the news form filling page where you need to specify the News Title, description, and select a photo

<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/29b4c071-b0ad-450a-ae57-34ee30dc05bc" />
If there are more news items than selected in the top right corner, a page navigation menu will appear at the bottom of the page

<img width="1227" height="756" alt="image" src="https://github.com/user-attachments/assets/422d3f4e-c605-4c85-b86a-11170e5034b7" />