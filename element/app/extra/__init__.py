from flask import Blueprint

extra = Blueprint('extra', __name__)

from . import models, views, errors