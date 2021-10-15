# Basketball Management System

## Description
This repository is all about to handle Model related operations.
Runs with [Python 3.6](https://www.python.org/downloads/release/python-360/).
It expose REST API for a Basketball Management System which has 3 users as League Admin,
Coach and Player.

#### primary frameworks

 - [Django](https://www.djangoproject.com/) :- Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.
 - [Django REST framework](https://www.django-rest-framework.org/) :- Django REST framework is a powerful and flexible toolkit for building Web APIs.

## Data
Service uses sqlite as an in memory DB to store related information.

## Development
```
# install virtual environment
pip install virtualenv

# setup virtual environment
virtualenv --python=/usr/bin/python3 venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run test cases - This command must be run in order to run the test cases
export DJANGO_SETTINGS_MODULE=yasara_answer.settings
python manage.py test

# migrate DB
python manage.py migrate_schemas

# create fake data to models
python manage.py createdata

## User credentials - To run APIs (Not test cases)
Admin: User name - admin
       Password - Admin123

Coach: User name - User name is displayed when the fake data is creating with 
                   corresponding user type. (Ex: player, coach)
       Password - 123

Player: User name - User name is displayed when the fake data is creating with 
                   corresponding user type. (Ex: player, coach)
       Password - 123

# run RPC server
python manage.py server

# run API server
python manage.py runserver 0.0.0.0:8000

# screenshots
screenshots of results have been added after running the APIs 
```

