from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# configure our database
db = SQLAlchemy(app)
# Flask utilizes sqlite3 with the use of SQLAlchemy
api = Api(app)

class TemplateModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100), nullable=False)

template_args = reqparse.RequestParser()
template_args.add_argument("body", type=str, required=True)

templateFields = {
    "id":fields.Integer,
    "body":fields.String
}

class Templates(Resource):
    @marshal_with(templateFields)
    def get(self):
        templates = TemplateModel.query.all()
        return templates

    @marshal_with(templateFields)
    def post(self):
        args = template_args.parse_args()
        template = TemplateModel(args["body"])
        db.session.add(template)
        db.session.commit()
        return 201

class Template(Resource):
    @marshal_with(templateFields)
    def get(self, id):
        template = TemplateModel.query.filter_by(id=id).first()
        if not template:
            abort(404, message="Template not found")
            return template

    def patch(self, id):
        args = template_args.parse_args()
        template = TemplateModel.query.filter_by(id=id).first()



class NotificationModel(db.Model):
    ...

# api.add_resource(Notification, "/api/notification")
# api.add_resource(Notification, "/api/notification/<int:id>")

api.add_resource(Template, "/api/templates")
# GET all templates
api.add_resource(Template, "/api/templates/<int:id>")
# POST new template
api.add_resource(Template, "/api/template/<int:id>")
# GET specific template
# PATCH update a specific template

if __name__ == "__main__":
    app.run(debug=True)
# in development we're good to set debug to True, but production we'd want False
