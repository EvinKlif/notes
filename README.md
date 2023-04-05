# Notebook

1. Clone the repository:
```bash
git clone https://github.com/EvinKlif/notes.git
```
2. Create and activate a virtual environment

3. Install dependencies from file ***requirements.txt***:
```bash
pip install -r requirements.txt
```

4. Go to folder:
```bash
cd notepad
```

5. Create application migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the app:
```bash
python manage.py runserver
```

7. The application will be available at: http://127.0.0.1:8000/
