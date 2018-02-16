#!flask/bin/python
from flask import Flask, jsonify
import datetime
import random

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


randNames = ["Robert Baratheon", "Jaime Lannister", "Catelyn Stark", "Cersei Lannister", "Daenerys Targaryen",
             "Jorah Mormont", "Viserys Targaryen", "Jon Snow", "Sansa Stark", "Arya Stark", "Robb Stark",
             "Theon Greyjoy"]

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
    "status": "failure",
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
    "estimatedTotalSeconds": 123456799,
    "elapsedTotalSeconds": 123456799,
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
def getServices():
    response = getResponse();
    response['commitedBy'] = "Daenerys Targaryen";
    return jsonify(response);


@app.route('/api/discovery/develop', methods=['GET'])
def getDiscovery():
    response = getResponse();
    response['commitedBy'] = "Arya Stark";
    return jsonify(response);


@app.route('/api/maintenance/develop', methods=['GET'])
def getmaintenance():
    response = getResponse();
    response['commitedBy'] = "Lord Varys";
    return jsonify(response);


stats = {
    "cpu": None,
    "memory": None,
    "diskspace": None
}

database = {
    "database": None
}

ingestion = {
    "ingestion": None
}


@app.route('/api/stats', methods=['GET'])
def getStats():
    cpu = random.randint(1, 100)
    stats['cpu'] = cpu;
    memory = random.randint(1000, 10000000)
    stats['memory'] = memory;
    diskspace = random.randint(10000, 1000000000)
    stats['diskspace'] = diskspace;
    return jsonify(stats);


@app.route('/api/database', methods=['GET'])
def getDatabase():
    rand = random.randint(1, 3)
    database["database"] = "UP";
    if rand == 2:
        database["database"] = "DOWN";
    if rand == 3:
        database["database"] = "INDEXING";
    return jsonify(database);


@app.route('/api/ingestionStats', methods=['GET'])
def getIngestionStats():
    string = 'Consumed ';
    files = random.randint(1, 1000)
    string += str(files);
    string += " files in ";
    minutes = random.randint(1, 120)
    string += str(minutes);
    string += " minutes";
    ingestion["ingestion"] = string;
    return jsonify(ingestion);


sonar = {
    "commitedBy": None,
    "coverage": None,
    "vulnerabilities": None,
    "codeSmells": None,
    "bugs": None,
    "timestamp": None
}


@app.route('/api/sonar/develop', methods=['GET'])
def getSonar():
    commitedBy = randNames[random.randint(1, len(randNames) - 1)];
    sonar["commitedBy"] = commitedBy;
    converage = random.randint(1, 100)
    sonar["coverage"] = converage;
    vulnerabilities = random.randint(1, 1000)
    sonar["vulnerabilities"] = vulnerabilities;
    codeSmells = random.randint(1, 1000)
    sonar["codeSmells"] = codeSmells;
    bugs = random.randint(1, 1000)
    sonar["bugs"] = bugs;
    sonar['timestamp'] = datetime.datetime.now();
    return jsonify(sonar);


if __name__ == '__main__':
    app.run(debug=True)
