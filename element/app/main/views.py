# -*- coding:utf-8 -*-

from flask.ext.restful import Api
from .models import JbossAPI

def init_views(app):
    api = Api(app)
    api.add_resource(JbossAPI, '/jboss/<int:id>')