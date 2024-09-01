from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
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

class Template(Resource):
    @marshal_with(templateFields)
    def get(self, id=None):
        if id is None:
        # if no id is passed in the request, return all templates
            templates = TemplateModel.query.all()
            return templates
        else:
        # an id is passed in the request; search for it and handle accordingly
            template = TemplateModel.query.filter_by(id=id).first()
            if not template:
                abort(404, message="Template not found")
            return template

    @marshal_with(templateFields)
    def post(self):
        args = template_args.parse_args()
        template = TemplateModel(body=args["body"])
        db.session.add(template)
        db.session.commit()
        return template, 201

    @marshal_with(templateFields)
    def patch(self, id):
        template = TemplateModel.query.filter_by(id=id).first()
        if not template:
            abort(404, message="Template not found")
        args = template_args.parse_args()
        template.body = args["body"]
        db.session.commit()
        return template


# class NotificationModel(db.Model):
#     ...


api.add_resource(Template, "/api/template", "/api/template/<int:id>")
# api.add_resource(Notification, "/api/notification", "/api/notification/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
# in development we're good to set debug to True, but production we'd want False
