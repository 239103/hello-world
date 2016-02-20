# -*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.restful import Resource
from .. import db

class JbossAPI(Resource):
    def get(self, int_id):
        query1 = Jboss()
        return {'hello': 'jboss' + queryl}
    
class Jboss(db.Model):
    __tablename__ = 'appjboss'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    
    def __repr__(self):
        return self.name
        
        

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r Emp_ID %s>' %self.name %self.emp_id

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')
    
    def __repr__(self):
        return '<Role %r>' % self.name