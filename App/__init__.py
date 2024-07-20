

# importing flask module to get the Flask class 
from flask import Flask

# importing flask sqlalchemy to get the sqlalchemy class for creating tables
from flask_sqlalchemy import SQLAlchemy

# calling the config file to call the Config class
from .config import Config

db=SQLAlchemy() # database object

# a function to intialize the app and database
def create_app():
    app=Flask(__name__)
    
    app.config.from_object(Config)
    

    db.init_app(app)

    from .routes import main as main_blueprint #calling routes file for getting the blueprint of data
    app.register_blueprint(main_blueprint)

    from .errors import error as errors_blueprint # calling error file to get error blueprint
    app.register_blueprint(errors_blueprint)

    return app
