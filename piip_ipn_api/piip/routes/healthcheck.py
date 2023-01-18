from piip.command.prueba import prueba
from piip.routes.resource import PIIPResource


class HealthCheck(PIIPResource):
    def get(self):
        """
        msg = Message("FROM PIIP",
                  recipients=["vomab30234@nifect.com"])
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail = current_app.config["MAIL_THING"]
        mail.send(msg)
        """
        school = prueba()
        return {"Success": f"{school.id}"}
