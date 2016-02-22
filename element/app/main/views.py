# -*- coding:utf-8 -*-

from flask.ext.restful import Api, Resource
from .models import Jboss

class JbossAPI(Resource):
    def get(self, strJbossName):
        objJboss = Jboss(strJbossName)
        return objJboss.Status

def init_apis(app):
    api = Api(app)
    api.add_resource(JbossAPI, '/jboss/<string:strJbossName>')