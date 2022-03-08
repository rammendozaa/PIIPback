from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from flask import Flask
from datetime import datetime, timedelta, timezone
import json
from flask_restful import Api
from piip.routes.healthcheck import HealthCheck
from piip.routes import (
    LogOut,
    Token,
    HealthCheck,
    Problems,
    SubmitProblem,
    Submission,
)

from scrapy.crawler import CrawlerProcess
from piip.services.providers.codeforces.codeforcesCrawler import CodeforcesSpider, getUrls


def create_application(name):

    app = Flask(name)
    app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

    jwt = JWTManager(app)

    app.config['JSON_SORT_KEYS'] = False

    """
    process = CrawlerProcess()
    process.crawl(CodeforcesSpider, urls=getUrls())
    process.start()
    """

    USERNAME = "root"
    PASSWORD = "root"
    HOST = "127.0.0.1"
    DATABASE = "PIIP_pruebas"

    database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_route

    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                data = response.get_json()
                if type(data) is dict:
                    data["access_token"] = access_token 
                    response.data = json.dumps(data)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response

    api = Api(app)
    api.add_resource(HealthCheck, "/")

    api.add_resource(Problems, "/problems")
    api.add_resource(SubmitProblem, "/problem/submit/<int:problem_id>")    
    api.add_resource(Submission, "/submission/")

    api.add_resource(Token, "/token")

    api.add_resource(LogOut, "/logout")

    return app