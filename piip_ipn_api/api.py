from flask import Flask,jsonify
import time

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/problems')
def getAllProblems():
    return jsonify([
        {"title" : "p1", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        {"title" : "p3", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
        {"title" : "p", "related_topics" : "dp, greedy", "difficulty" : "easy", "status" : "solved"},
    ])