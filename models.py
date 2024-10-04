from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, reqparse, fields


# app configuration and initialization
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
api = Api(app)


# TEMPLATE TABLE
class TemplateModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(100), nullable = False)

template_args = reqparse.RequestParser()
template_args.add_argument("body", type = str, required = True, help = "Body is required")
# ^ required = True and help = will error-handle no data being passed in the call and assist with a message 

templateFields = {
    "id": fields.Integer,
    "body": fields.String
}


# NOTIFICATION TABLE 
class NotificationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), nullable=False)
    personalization = db.Column(db.String(100), nullable=True)
    template_id = db.Column(db.Integer, db.ForeignKey("template_model.id"), nullable = False)
    # ^ creating a foreign key constraint that links template_id in NotificationModel to the id field in TemplateModel
    template = db.relationship("TemplateModel", backref = db.backref("notifications", lazy = True, cascade = "all, delete-orphan"))
    # ^ seting up a relationship between the NotificationModel and TemplateModel allowing access to the related TemplateModel 
    # from a NotificationModel instance, using notification.template

notification_args = reqparse.RequestParser()
notification_args.add_argument("phone_number", type = str, required = True, help = "Phone number is required")
notification_args.add_argument("personalization", type = str, required = False)
notification_args.add_argument("template_id", type = int, required = True, help = "Template ID is required")

notificationFields = {
    "id": fields.Integer,
    "phone_number": fields.String,
    "personalization": fields.String,
    "template_id": fields.Integer
}
