sudo pip3 install virtualenv
sudo pip install autoenv
virtualenv apienv
source apienv/bin/activate
pip install -r requirements.txt 
createdb test_db
createdb flask_api
python manage.py db migrate
python manage.py db upgrade
flask run
python test_recipes.py
