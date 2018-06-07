sudo pip3 install virtualenv
sudo pip3 install autoenv
virtualenv -p python3 apienv
source apienv/bin/activate
pip3 install -r requirements.txt
createdb test_db
createdb flask_api
python manage.py db migrate
python manage.py db upgrade
flask run
python test_recipes.py
