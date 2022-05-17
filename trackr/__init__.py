from os import environ
from flask import Flask
from trackr.db import db
from flask_migrate import Migrate
from trackr import items

def create_app():
	# create and configure the app
	app = Flask(__name__)
	app.config.from_object("config.Config")
	mode = environ.get("MODE")
	if mode == "production":
		app.config.from_object("config.ProdConfig")

	# db
	db.init_app(app)
	migrate = Migrate()
	migrate.init_app(app, db)
	
	# bp
	app.register_blueprint(items.bp)
	app.add_url_rule("/", endpoint = "index")
	
	return app
	