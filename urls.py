from models import api
from api import Template, Notification

api.add_resource(Template, "/api/template", "/api/template/<int:id>")
api.add_resource(Notification, "/api/notification", "/api/notification/<int:id>")
