from email.policy import default
from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from piip.models.administrator import Administrator
from providers.codeforces.codeforces import Codeforces
import random

app = Flask(__name__)

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