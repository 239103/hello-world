import os

from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

class jboss_app(db.Model):
    __tablename__ = 'jboss_app'
    id = db.Column(db.Interger, primary_key=True)
    cmdb_name = db.Column(db.String(64), index=True)

