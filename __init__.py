from apiflask import APIFlask, Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import os
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import DeclarativeBase
#from flask.views import MethodView


#class Base(DeclarativeBase):
#  pass

#From Flask Tutorial to have an Application Factory function
def create_app(test_config=None):
#    db = SQLAlchemy(model_class=Base)
    app = APIFlask(__name__, instance_relative_config=True)
    # Initialize SQLAlchemy
    app.config.from_mapping(
        SECRET_KEY = 'dev',
 #       SQLALCHEMY_DATABASE_URI = 'sqlite:////project.db'
    )
 #   db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #API Flask app
    @app.get('/')
    def index():
        return {'message': 'hello'}

    @app.get('/pets')
    def get_pets():
        return {'message': 'OK'}

    @app.post('/pets')
    def create_pet():
        return {'message': 'created'}, 201

    @app.put('/pets/<int:pet_id>')
    def update_pet(pet_id):
        return {'message': 'updated'}

    @app.delete('/pets/<int:pet_id>')
    def delete_pet(pet_id):
        return '', 204

    return app

# Create data storage


#class Person(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String)
#    email = db.Column(db.String)
#    birth_date = db.Column(db.Date)
#    password = db.Column(db.String)
#
#
#class Computer(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    serial = db.Column(db.String)
#    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#    person = db.relationship('Person', backref=db.backref('computers'))

