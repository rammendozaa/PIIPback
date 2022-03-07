from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from email.policy import default
from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from piip.models.administrator import Administrator
from providers.codeforces.codeforces import Codeforces
from datetime import datetime, timedelta, timezone
import json
import random

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
DATABASE = "PIIP_pruebas"

CF_USERNAME = "Barbosa1998"
CF_PASSWORD = "Barbosa20111910";

database_route = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
app.config["SQLALCHEMY_DATABASE_URI"] = database_route
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
session = db.session


@app.route("/")
def index():
    dict_school = session.query(Administrator).get(1)
    print(f"Administrator name: {dict_school.first_name}")
    return ""


@app.route('/problems')
@jwt_required()
def getAllProblems():
    return jsonify([
        {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        {"title" : "p2", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
    ])

@app.route('/problem/submit')
def submitProblem():
    codeforces = Codeforces()
    codeforces.login(CF_USERNAME, CF_PASSWORD)
    if codeforces.check_login():
        submissionUrl = codeforces.submit('1254A', 'qwer' + str(random.random()) )
        return {"submissionUrl": submissionUrl}
    else:
        return {"submissionUrl": "failed"}

@app.route('/submission/')
def getSubmissionStatus():
    submissionUrl = request.args.get('submissionUrl',default='',type=str)
    codeforces = Codeforces()
    codeforces.login(CF_USERNAME, CF_PASSWORD)
    if codeforces.check_login():
        status = codeforces.getSubmissionStatus(submissionUrl)
        return {"status": status}
    else:
        return {"status": "failed to login"}

@app.route('/token', methods=["POST"])
def create_token():
    email = request.form.get("email", default='',type=str)
    password = request.form.get("password", default='',type=str)
    if email == "hugo" and password == "hugo":
        access_token = create_access_token(identity=email)
        response = {"access_token":access_token, "role": "mentor"}
        return response
    if email == "alvaro" and password == "alvaro":
        access_token = create_access_token(identity=email)
        response = {"access_token":access_token, "role": "user"}
        return response
    return {"msg": "Wrong email or password"}, 401

@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

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