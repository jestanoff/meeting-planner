# Meeting planner
Simple meeting application that helped me learn Django

## Requirements
- At least Python 3.6 - follow the instructions on https://realpython.com/installing-python/
- Virtualenv - follow the instructions on https://virtualenv.pypa.io/en/stable/installation.html

## Installation
In your terminal of choose follow these instructions
1. Cretate virtual environment to isolate your python project
```
$ virtualenv .venv -p python3.6 
```
2. Activate the virtual environment
```
$ source .venv/bin/activate
```
3. Install django
```
$ python -m pip install Django
```
4. Run migrations
```
$ python manage.py migrate
```
5. Create admin super user
```
$ python manage.py createsuperuser
```
Follow the questions in the terminal to create an admin
6. Run the web server
```
$ python manage.py runserver
```
