#!flask/bin/python
from flask import Flask, jsonify
import datetime
import random

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


orchestrationSuccess = {
    "status": "success",
    "commitedBy": "Johns Snow",
    "build": 12341,
    "timestamp": None,
    "branch": "develop",
    "pendingChanges": [
        {
            "commitBy": "Tyrion Lannister",
            "changeId": 41231
        },
        {
            "commitBy": "Robb Stark",
            "changeId": 12311
        }
    ]
}

orchestrationFail = {
    "status": "fail",
    "commitedBy": "Johns Snow",
    "build": 12134,
    "timestamp": None,
    "branch": "develop",
    "pendingChanges": [
        {
            "commitBy": "Tyrion Lannister",
            "changeId": 1221
        },
        {
            "commitBy": "Viserys Targaryen",
            "changeId": 31231
        },
        {
            "commitBy": "Tyrion Lannister",
            "changeId": 1211
        },
        {
            "commitBy": "Viserys Targaryen",
            "changeId": 312311
        },
        {
            "commitBy": "Tyrion Lannister",
            "changeId": 112221
        },
        {
            "commitBy": "Viserys Targaryen",
            "changeId": 312231
        },

    ]
}

orchestrationRunning = {
    "status": "running",
    "commitedBy": "Johns Snow",
    "build": 4325,
    "timestamp": None,
    "branch": "develop",
    "estimatedTotalSeconds" : 123456799,
    "elapsedTotalSeconds" : 123456799,
    "pendingChanges": [
        {
            "commitBy": "Sansa Stark",
            "changeId": 6544
        },
        {
            "commitBy": "Khal Drogo",
            "changeId": 758
        }
    ]
}


def getResponse():
    rand = random.randint(1, 3)
    response = orchestrationSuccess;
    if rand == 2:
        response = orchestrationFail;
    if rand == 3:
        response = orchestrationRunning;
    response['timestamp'] = datetime.datetime.now();
    return response;


@app.route('/api/orchestration/develop', methods=['GET'])
def getOrchestration():
    response = getResponse();
    return jsonify(response);


@app.route('/api/ingestion/develop', methods=['GET'])
def getIngestion():
    response = getResponse();
    response['commitedBy'] = "Robb Stark";
    return jsonify(response);


@app.route('/api/core/develop', methods=['GET'])
def getCore():
    response = getResponse();
    response['commitedBy'] = "Viserys Targaryen";
    return jsonify(response);


@app.route('/api/commons/develop', methods=['GET'])
def getCommons():
    response = getResponse();
    response['commitedBy'] = "Ned Stark";
    return jsonify(response);


@app.route('/api/security/develop', methods=['GET'])
def getSecurity():
    response = getResponse();
    response['commitedBy'] = "Joffrey Baratheon";
    return jsonify(response);


@app.route('/api/maintenance/develop', methods=['GET'])
def getMaintenance():
    response = getResponse();
    response['commitedBy'] = "Theon Greyjoy";
    return jsonify(response);


@app.route('/api/registration/develop', methods=['GET'])
def getRegistration():
    response = getResponse();
    response['commitedBy'] = "Jaime Lannister";
    return jsonify(response);


@app.route('/api/portal/develop', methods=['GET'])
def getPortal():
    response = getResponse();
    response['commitedBy'] = "Cersei Lannister";
    return jsonify(response);


@app.route('/api/services/develop', methods=['GET'])
def getService():
    response = getResponse();
    response['commitedBy'] = "Daenerys Targaryen";
    return jsonify(response);


if __name__ == '__main__':
    app.run(debug=True)
