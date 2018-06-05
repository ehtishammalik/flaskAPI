# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    from app.models import Recipes
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/recipes/', methods=['POST', 'GET'])
    def recipes():
        if request.method == "POST":
            name = str(request.data.get('name', ''))
            if name:

                recipe = Recipes(name=name)
                recipe.save()
                response = jsonify({
                    'id': recipe.id,
                    'name': recipe.name,
                    'prep_time': recipe.prep_time,
                    'difficulty': recipe.difficulty,
                    'vegetarian': recipe.vegetarian
                })
                response.status_code = 201
                return response

        else:
            # GET
            recipes = Recipes.get_all()
            results = []

            for recipe in recipes:
                obj = {
                'id': recipe.id,
                'name': recipe.name,
                'prep_time': recipe.prep_time,
                'difficulty': recipe.difficulty,
                'vegetarian': recipe.vegetarian
            }
            results.append(obj)


            response = jsonify(results)
            response.status_code = 200
            return response

    @app.route('/recipes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def recipe_manipulation(id, **kwargs):
        # retrieve a recipe using it's ID
        recipe = Recipes.query.filter_by(id=id).first()
        if not recipe:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            recipe.delete()
            return {
                       "message": "recipe {} deleted successfully".format(recipe.id)
                   }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            recipe.name = name
            recipe.save()
            response = jsonify({
                'id': recipe.id,
                'name': recipe.name,
                'prep_time': recipe.prep_time,
                'difficulty': recipe.difficulty,
                'vegetarian': recipe.vegetarian
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': recipe.id,
                'name': recipe.name,
                'prep_time': recipe.prep_time,
                'difficulty': recipe.difficulty,
                'vegetarian': recipe.vegetarian
            })
            response.status_code = 200
            return response

    return app
