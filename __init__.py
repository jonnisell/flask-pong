from apiflask import APIFlask, Schema
from apiflask.fields import Integer, String
from apiflask.validators import Length, OneOf
import os
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.orm import DeclarativeBase
#from flask.views import MethodView


#From Flask Tutorial to have an Application Factory function
def create_app(test_config=None):
#    db = SQLAlchemy(model_class=Base)
    app = APIFlask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'pingpong.sqlite'),
    )

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

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

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

