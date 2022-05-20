from flask import Blueprint

bp = Blueprint("items", __name__, template_folder = "templates")

from trackr.items import routes
