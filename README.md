# flaskAPI
A Recipes RESTful API build using python and flask. This API is [REST API](http://en.wikipedia.org/wiki/Representational_State_Transfer "RESTful"). Currently, return format for all endpoints is [JSON](http://json.org/ "JSON").
***
## Changes

### Commits on Jun 6, 2018
- Create README.md
- ignored files removed
- final commit
- adding .gitignore

### Commits on Jun 5, 2018
- All tests are passed. Database has been connected. CRUD requestes hav…  …
- First Test without functionality.All tests Failed as expected :)
- Migrations made and DB updated
- Recipes Model Created
- App successfully created

### Commits on Jun 4, 2018
- First Commit


## Endpoints

- GET /recipes/
- GET /recipes/id
- POST /recipes/
- PUT /recipes/id
- DELETE /recipes/id
- PUT /recipes/id/rating

## FAQ
### What do I need to know before I start using the API?
You need to know following things before using this api:

- HTTPS protocol
- Data serialization with [JSON][] (or see a [quick tutorial][])

### What are the return fomats of this api?
This API currently returns data in [JSON](http://json.org/ "JSON") format.

### How to change the postgres user and password?
- First, open instance/config.py edit the line 19. Change the user and password according to your user and password. It look like this: 
```
postgresql://user:password@localhost/test_db
```
- Now, open .env file in the main directory and edit the line 5. It has same pattern as above.
```
postgresql://user:password@localhost/flask_api
```
### How do I use it?
To use this api you need to follow these steps:

- Download or clone this project into your system.
- cd into the "flaskAPI-master" directory. This will run the autoenv in your system.
- check the requirements.txt to fulfill all the requirements. To auto install all the requirements run the bash command mentioned below.

- execute the "commands.sh" file by typing the following command on terminal to install all requirements:
```
. commands.sh
```
### Or
- run the following commands on your terminal:
```
sudo pip3 install virtualenv
sudo pip install autoenv
virtualenv apienv
source apienv/bin/activate
```
- now in your terminal run the following commands to create databases:
```
createdb test_db
createdb flask_api
```
- to install requirements manually run the following command:
```
sudo pip install -r requirements.txt
```
- now to migrate the models run the following commands in your terminal
```
python manage.py db migrate
```
the output of this command should be like this:
```
  INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
  INFO  [alembic.runtime.migration] Will assume transactional DDL.
  INFO  [alembic.autogenerate.compare] Detected added table 'results'
    Generating /bucketlist/migrations/versions/63dba2060f71_.py
    ...done
```

- now apply the migrations using this command:
```
python manage.py db upgrade
```
the output of this command should be like this:
```
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 536e84635828, empty messag
```
- to run the api type the following command in the terminal:
```
flask run
``` 
This will start the flask server on address: [http://127.0.0.1:5000/]
- API is up and running. You can make requests now.

- to run the tests type the following command on the terminal:
```
python test_bucketlist.py
```
the result of this command should be something like this:
```
Ran 5 tests in 0.31s

OK
```

## ACKNOWLEDGEMENTS
- https://www.youtube.com/watch?v=s_ht4AKnWZg
- https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
- https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way#api-functionality
- https://github.com/mjhea0/flaskr-tdd
- https://www.youtube.com/watch?v=WxGBoY5iNXY

