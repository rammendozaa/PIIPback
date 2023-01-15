from flask_restful import Resource

from piip.middleware.errors import error_handling


class PIIPResource(Resource):
    method_decorators = [error_handling]
