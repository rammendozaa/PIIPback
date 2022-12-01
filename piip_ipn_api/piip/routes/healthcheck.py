from flask_restful import Resource
from piip.command.prueba import prueba
from flask_mail import Message
from flask import current_app

class HealthCheck(Resource):
    def get(self):
        """
        msg = Message("FROM PIIP",
                  recipients=["vomab30234@nifect.com"])
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail = current_app.config["MAIL_THING"]
        mail.send(msg)
        """
        user = prueba()
        return {"is_all_good": f"YES. School: {user.description}"}
