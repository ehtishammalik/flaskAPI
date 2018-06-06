# app/models.py

from app import db


class Recipes(db.Model):
    """This class represents the Recipes table."""

    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    prep_time = db.Column(db.String(255))
    difficulty = db.Column(db.Integer)
    vegetarian = db.Column(db.Boolean)
    rating = db.Column(db.Integer)
    rating_numbering = db.Column(db.Integer)

    def __init__(self, name, prep_time, difficulty, vegetarian, rating):
        """initialize with name."""
        self.name = name
        self.prep_time = prep_time
        self.difficulty = difficulty
        self.vegetarian = vegetarian
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Recipes.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Recipes: {}>".format(self.name)
