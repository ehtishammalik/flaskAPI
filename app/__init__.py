# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort
from sqlalchemy.sql import func

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
    from app.models import Recipes

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/recipes/', methods=['POST', 'GET'])
    def recipes():
        if request.method == "POST":
            data = request.get_json()
            recipe_name = data['name']
            recipe = Recipes.query.filter_by(name=recipe_name).first()

            if not recipe:
                new_recipe = Recipes(name=data['name'], prep_time=data['prep_time'], difficulty=data['difficulty'],
                                     vegetarian=data['vegetarian'], rating=data['rating'])
                new_recipe.rating_numbering = 1
                new_recipe.save()
                response = jsonify({
                    'id': new_recipe.id,
                    'name': new_recipe.name,
                    'prep_time': new_recipe.prep_time,
                    'difficulty': new_recipe.difficulty,
                    'vegetarian': new_recipe.vegetarian,
                    'rating': new_recipe.rating
                })
                response.status_code = 201
                return response
            else:
                response = jsonify({'message': 'recipie already exist'})
                response.status_code = 304
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
            recipe = Recipes.query.filter_by(id=id).first()
            if not recipe:
                return jsonify({'message': 'No user found!'})

            recipe.admin = True
            db.session.commit()
            response = jsonify(recipe)
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                'id': recipe.id,
                'name': recipe.name,
                'prep_time': recipe.prep_time,
                'difficulty': recipe.difficulty,
                'vegetarian': recipe.vegetarian,
                'rating' : recipe.rating
            })
            response.status_code = 200
            return response

    @app.route('/recipes/<int:id>/rating', methods=['PUT'])
    def recipe_rating(id):
        data = request.get_json()
        rating = data['rating']
        print(rating)
        recipe = Recipes.query.filter_by(id=id).first()
        if not recipe:
            # Raise an HTTPException with a 404 not found status code
            abort(404)
        else:
            recipe.rating_numbering = int(recipe.rating_numbering) + 1
            print(recipe.rating_numbering)
            print((int(recipe.rating) + int(rating)))
            recipe.rating = (int(recipe.rating) + int(rating)) / 2
            print(recipe.rating)
            recipe.save()
            response = jsonify({
                'id': recipe.id,
                'name': recipe.name,
                'prep_time': recipe.prep_time,
                'difficulty': recipe.difficulty,
                'vegetarian': recipe.vegetarian,
                'rating': recipe.rating
            })
            response.status_code = 201
            return response

    return app
