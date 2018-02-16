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

red = 'RED'

yellow = 'YELLOW'

green = 'GREEN'

fiftyfive = '55'
seventy = '70'
ninety = '90'
thirty = '30'



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
    "diskspace": None,
    "timestamp": None,
    "ingestion":None,
    "database":None
}

database = {
    "database": None,
    "timestamp": None
}


@app.route('/api/stats', methods=['GET'])
def getStats():
    cpu = random.randint(1, 100)
    stats['cpu'] = str(cpu) + '% Consumed';
    memory = random.randint(1024, 3020)
    stats['memory'] = str(memory) + 'MB out of 4096MB consumed';
    diskspace = random.randint(10, 100)
    stats['diskspace'] = str(diskspace) + 'TB out of 150 TB is full';
    stats['timestamp'] = datetime.datetime.now();
    string = 'Consumed ';
    files = random.randint(1, 1000)
    string += str(files);
    string += " files in ";
    minutes = random.randint(1, 120)
    string += str(minutes);
    string += " minutes";
    stats["ingestion"] = string;

    rand = random.randint(1, 3)
    status = "MongoDB is "
    if rand == 1:
        stats["database"] = status + "UP";
    if rand == 2:
        stats["database"] = status + "DOWN";
    if rand == 3:
        stats["database"] = status + "INDEXING";

    return jsonify(stats);



sonar = {
    "commitedBy": None,
    "coverage": None,
    "vulnerabilities": None,
    "codeSmells": None,
    "bugs": None,
    "timestamp": None
}


@app.route('/api/sonar', methods=['GET'])
def getSonar():
    commitedBy = randNames[random.randint(1, len(randNames) - 1)];
    sonar["commitedBy"] = commitedBy;
    converage = str(random.randint(1, 100)) + '% Code Covered'
    sonar["coverage"] = converage;
    vulnerabilities = str(random.randint(1, 1000)) + ' found'
    sonar["vulnerabilities"] = vulnerabilities;
    codeSmells = str(random.randint(1, 1000)) + ' found'
    sonar["codeSmells"] = codeSmells;
    bugs = str(random.randint(1, 1000))
    sonar["bugs"] = bugs + ' found'
    sonar['timestamp'] = datetime.datetime.now();
    return jsonify(sonar);

@app.route('/app/teamcity/builds/buildType:(id:uds),branch:develop', methods=['GET'])
def get_developstatus():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return red
  if number == 2:
    return yellow
  if number == 3:
    return green

@app.route('/app/teamcity/builds/buildType:(id:uds),branch:uat', methods=['GET'])
def get_uatstatus():
  number = random.randint(1, 3)
  print number
  if number == 1:
    return red
  if number == 2:
    return yellow
  if number == 3:
    return green

@app.route('/app/teamcity/builds/buildType:(id:cpumotor),branch:develop', methods=['GET'])
def get_cpumotor():
  number = random.randint(1, 4)
  print number
  if number == 1:
    return fiftyfive
  if number == 2:
    return thirty
  if number == 3:
    return seventy
  if number == 4:
    return ninety

@app.route('/app/teamcity/builds/buildType:(id:memorymotor),branch:develop', methods=['GET'])
def get_memorymotor():
  number = random.randint(1, 4)
  print number
  if number == 1:
    return fiftyfive
  if number == 2:
    return thirty
  if number == 3:
    return seventy
  if number == 4:
    return ninety


if __name__ == '__main__':
    app.run(debug=True)
