from os import environ, path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))

load_dotenv(path.join(base_dir, ".env"))

class Config(object):
    FLASK_APP = "trackr"
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")
    