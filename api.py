from flask_restful import Resource, marshal_with, abort
from models import TemplateModel, NotificationModel, templateFields, template_args, notificationFields, notification_args, db, app
import urls


# TEMPLATE GET/POST/PATCH/DELETE
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


# NOTIFICATION GET/POST/DELETE
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

if __name__ == "__main__":
    app.run(debug=False)
# for production = False, Development = True