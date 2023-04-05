Clone the repository:
    git clone https://github.com/EvinKlif/notes.git
Create and activate a virtual environment

Install dependencies from file requirements.txt:

pip install -r requirements.txt

Go to folder:

cd notepad
Create application migrations:
   python manage.py makemigrations
   python manage.py migrate
Run the app:
   python manage.py runserver
The application will be available at: http://127.0.0.1:8000/
