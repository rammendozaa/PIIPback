from flask_restful import Resource

from piip.command.prueba import prueba

class HealthCheck(Resource):
    def get(self):
        print("hola")
        user = prueba()
        return {"is_all_good": f"YES. School: {user.description}"}
