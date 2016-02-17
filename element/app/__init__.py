#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask import Blueprint

app = Blueprint('app', __name__)
sys.path.append("app");
sys.path.append("app/views");
sys.path.append("app/models");
from views import *
from models import *

def create_app(config_name):
    from .app import app as app_blueprint
    app.register_blueprint(app_blueprint)
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    
    return app

