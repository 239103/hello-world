# -*- coding:utf-8 -*-

from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.Interger)
    role_id = db.Column(db.integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r Emp_ID %s>' %self.name %self.emp_id
    
    
    