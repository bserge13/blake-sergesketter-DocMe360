from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# app, database, and api configuration/setup/connection
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
api = Api(app)

# Tables 
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

# Class-functions
class Template(Resource):
    @marshal_with(templateFields)
    def get(self, id = None):
        if id is None:
        # ^ no id is passed in the request, return all templates
            templates = TemplateModel.query.all()
            return templates
        else:
        # ^ an id is passed in the request, we search for it and handle accordingly from that point
            template = TemplateModel.query.filter_by(id = id).first()
            if not template:
                abort(404, message="Template not found")
            return template

    @marshal_with(templateFields)
    def post(self):
        args = template_args.parse_args()
        template = TemplateModel(body = args["body"])
        db.session.add(template)
        db.session.commit()
        return template, 201

    @marshal_with(templateFields)
    def patch(self, id):
        template = TemplateModel.query.filter_by(id = id).first()
        if not template:
            abort(404, message = "Template not found")
        args = template_args.parse_args()
        template.body = args["body"]
        db.session.commit()
        return template

    @marshal_with(templateFields)
    def delete(self, id):
        template = TemplateModel.query.filter_by(id = id).first()
        if not template:
            abort(404, message = "Template not found")
        db.session.delete(template)
        db.session.commit()

class Notification(Resource):
    def get(self, id = None):
        if id is None:
            notifications = NotificationModel.query.all()
            return [{
                "id": note.id,
                "phone_number": note.phone_number,
                "personalization": note.personalization,
                "template_id": note.template_id,
            } for note in notifications]
        else:
            notification = NotificationModel.query.filter_by(id=id).first()
            if not notification:
                abort(404, message = "Notification not found")

            template = notification.template
            if not template:
                abort(404, message = "Template not found")
            content = template.body.replace("(personal)", notification.personalization or "")

            return {
                "id": notification.id,
                "phone_number": notification.phone_number,
                "personalization": notification.personalization,
                "template_id": notification.template_id,
                "content": content,
            }

    @marshal_with(notificationFields)
    def post(self):
        args = notification_args.parse_args()
        notification = NotificationModel(
            phone_number = args["phone_number"],
            personalization = args["personalization"],
            template_id = args["template_id"]
            )
        db.session.add(notification)
        db.session.commit()
        return notification, 201

    @marshal_with(notificationFields)
    def delete(self, id):
        notification = NotificationModel.query.filter_by(id = id).first()
        if not notification:
            abort(404, message = "Notification not found")
        db.session.delete(notification)
        db.session.commit()

# Resources/routes for api consumption
api.add_resource(Template, "/api/template", "/api/template/<int:id>")
api.add_resource(Notification, "/api/notification", "/api/notification/<int:id>")

if __name__ == "__main__":
    app.run(debug=False)
# for production = False, Development = True