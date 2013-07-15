from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.nytro import Blueprint
from sample_app import settings

#Creates a SQLAlchemy instance for flask app
db = SQLAlchemy()

def create_app(config=settings):
    #Creates an app
    app = Flask(__name__)

    #Loads config to app
    app.config.from_object(config)

    #Attaches all blueprints to app automatically by convention or configuration
    Blueprint.attach_all(app)

    #Prepares and initializes the database for the app
    db.init_app(app)

    return app