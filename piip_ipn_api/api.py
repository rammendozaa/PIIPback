from flask import Flask,jsonify
import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from piip.models.administrator import Administrator

app = Flask(__name__)

USERNAME = "root"
PASSWORD = "root"
HOST = "127.0.0.1"
DATABASE = "PIIP_pruebas"

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
