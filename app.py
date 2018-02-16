#!flask/bin/python
from flask import Flask, jsonify
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
			"commitedBy": "Jaime Lannister",
			"build": 12134,
			"timestamp": None,
			"pendingChanges": [
				{
					"commitBy": "Tyrion Lannister",
					"changeId": 1221
				},
				{
					"commitBy": "Viserys Targaryen",
					"changeId": 31231
				}
			]
		}
		
orchestrationRunning = {
				"status": "running",
				"commitedBy": "Theon Greyjoy",
				"build": 4325,
				"timestamp": None,
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
			

@app.route('/api/orchestration', methods=['GET'])
def get_tasks():
	rand = random.randint(1,3)
	response = orchestrationSuccess;
	if rand == 2:
		response = orchestrationFail;
	if rand == 3:
		response = orchestrationRunning;
	return jsonify(response);


if __name__ == '__main__':
    app.run(debug=True)