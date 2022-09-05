from os import environ
from flask import Flask
from config import Config, ProdConfig
from trackr.db import db
from flask_migrate import Migrate
from trackr import errors
from werkzeug.exceptions import HTTPException
from trackr.items import bp as items_bp


def create_app():
    # create and configure the app
    app = Flask(__name__)
    mode = environ.get("MODE")
    if mode == "development":
        app.config.from_object(Config)
    if mode == "production":
        app.config.from_object(ProdConfig)

    # db
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    # error handlers
    app.register_error_handler(HTTPException, errors.handle_error)

    # bp
    app.register_blueprint(items_bp)
    app.add_url_rule("/", endpoint="index")

    return app
