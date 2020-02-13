# mynews

## Usage

1. Install Python 3.5 or newer
2. Install extra project modules by issuing the following command from the terminal:

    ```
    cd "C:\path\to\the\project\folder"
    pip install -r requirements.txt
    ```
3. Rename "mynews/local_settings.py.template" to "mynews/local_settings.py"
   and replace the placeholder configurations.

4. Apply migrate:

    ```
    python manage.py migrate
    ```
5. Create "superuser":

    ```
    python manage.py createsuperuser
    ```
6. Install and run redis. You can use docker:

    ```
    docker run --name mynews-redis --publish 6379:6379 -d redis:alpine
    ```
7. Run celery worker in new terminal:

    ```
    cd "C:\path\to\the\project\folder"
    celery worker -A mynews
    ```
8. Start server:

    ```
    python manage.py runserver
    ```
