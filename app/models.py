# app/models.py

from app.init import db

class Recipes(db.Model):
    """This class represents the Recipes table."""

    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    prep_time = db.Column(db.String(255))
    difficulty = db.Column(db.Integer)
    vegetarian = db.Column(db.Boolean)

    def __init__(self, name):
        """initialize with name."""
        self.name = name

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
