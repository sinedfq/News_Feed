<h1>Лента новостей (SIBERS)</h1>

<h3>Стек:</h3>

1. Python
2. Django
3. HTML/CSS
4. PostgreSQL

-----

<h3>Инструкция по запуску: </h3>

1. Создать базу данных PostgreSQL с названием ``` news_feed_db ``` через PgAdmin или коммандную строку.
2. Перейти в главную папку проекта ``` news_project ``` и при необходимости создать виртуальное окружение ``` python -m venv venv ```
3. Установить необходимые компоненты проекта при помощи команды ``` pip install requrments.txt ```
4. Выполнить создание миграций ``` python manage.py makemigrations ```
5. Выполнить созданные миграции ``` python manage.py migrate ```
6. В случае успешного выполнения запустить проект ``` python manage.py runserver ```

<h3>База данных: </h3>

В проекте используется СУБД PostgreSQL и для успешного функционирования проекта необходимо создать саму базу данных и указать логин и пароль от СУБД. <br>
Создать базу данных можно 2 способами: 

1. Через приложение PgAdmin
<img align = "center" width="1458" height="946" alt="image" src="https://github.com/user-attachments/assets/1b8645b1-81aa-47b6-a14a-1e0077d2adab" />
<img align = "center" width="1458" height="945" alt="image" src="https://github.com/user-attachments/assets/beb1bfe6-92ba-43c2-b59d-abd40fdaa758" />

<br>

2. Через командную строчку <br>
Необходимо перейти в путь, куда установлен PostgreSQL и запустить следующей командой консоль: ```psql -U postgres``` <br>
Выполнить создание таблицы командой ``` CREATE DATABASE news_feed_db; ``` <br>


Если ваше имя пользователя или пароль отличается измените их в settings.py в полях указанных ниже: <br>
settings.py
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_feed_db', // НАЗВАНИЕ БАЗЫ ДАННЫХ
        'USER': 'postgres',     // ИМЯ ПОЛЬЗОВАТЕЛЯ
        'PASSWORD': '1234',     // ПАРОЛЬ ПОЛЬЗОВАТЕЛЯ
        'HOST': 'localhost',    // АДРЕСС ЛОКАЛЬНОГО СЕРВЕРА
        'PORT': '5432',         // ПОРТ ЛОКАЛЬНОГО СЕРВЕРА
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

```

------

При необходимости поменять дизайн веб-приложения воспользуйтесь полем <styles> в html разметке