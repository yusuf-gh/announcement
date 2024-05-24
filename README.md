# announcement

Открой терминал...

1. Создание виртуального окружения(а если оно не установлен то сперва "pip install virtualenv").

    python -m venv venv

2. Активация виртуального окружения.

    venv\Scripts\activate

3. Установка зависимотсей...

    pip install -r requirements.txt

4. Миграции базы данных

    python manage.py makemigrations
    _______________________________

    python manage.py migrate

5. Создание супер-юзера.

    python manage.py createsuperuser


6. Запуск сервера

    python manage.py runserver

