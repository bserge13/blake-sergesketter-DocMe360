from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# configure our database
db = SQLAlchemy(app)
# Flask utilizes sqlite3 with the use of SQLAlchemy 

class TemplateModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=True)

template_args = reqparse.RequestParser()


if __name__ == "__main__":
    app.run(debug=True)
# in development we're good to set debug to True, but production we'd want False
