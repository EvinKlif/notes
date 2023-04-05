1. Clone the repository:
     git clone https://github.com/EvinKlif/notes.git
2. Create and activate a virtual environment

   Install dependencies from file requirements.txt:

   pip install -r requirements.txt

3.Go to folder:
  cd notepad

4.Create application migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Run the app:
   python manage.py runserver
The application will be available at: http://127.0.0.1:8000/
