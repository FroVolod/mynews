# mynews

## Usage

1. Install Python 3.5 or newer
2. Install extra project modules by issuing the following command from the terminal:

    ```
    cd "C:\path\to\the\project\folder"
    pip install -r requirements.txt
    ```
3. Create "superuser":

    ```
    python manage.py createsuperuser
    ```
4. Apply migrate:

    ```
    python manage.py migrate
    ```
5. Rename "mynews/local_settings.py.template" to "mynews/local_settings.py"
   and replace the placeholder configurations.

6. Start server:

    ```
    python manage.py runserver
    ```
