virtualenv apienv
source apienv/bin/activate
createdb test_db
createdb flask_api
python manage.py db migrate
python manage.py db upgrade
flask run
python test_recipes.py
