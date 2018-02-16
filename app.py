#!flask/bin/python
from flask import Flask

app = Flask(name)

@app.route('/')
def index():
return "Hello, World!"

tasks = [
{
"actions": [
{
"causes": [
{
"shortDescription": "Started by an SCM change"
}
]
},
{},
{},
{}
],
"artifacts": [],
"building": False,
"description": None,
"duration": 80326,
"estimatedDuration": 68013,
"executor": None,
"fullDisplayName": "my project #149",
"id": "2013-06-14_14-31-06",
"keepLog": False,
"number": 149,
"result": "SUCCESS",
"timestamp": 1371234666000,
"url": "http://localhost:8080/job/my project/149/",
"builtOn": "",
"changeSet": {
"items": [
{
"affectedPaths": [
"SearchViewController.m",
"Sample.strings"
],
"author": {
"absoluteUrl": "http://localhost:8080/user/my user",
"fullName": "My User"
},
"commitId": "9032",
"timestamp": 1371234304048,
"date": "2013-06-14T18:25:04.048031Z",
"msg": "Author:my_author Description: changes Id: B-186199 Reviewer:reviewer_name",
"paths": [
{
"editType": "edit",
"file": "/branches/project_name/iOS/_MainLine/project_name/SearchViewController.m"
},
],
"revision": 9032,
"user": "user_name"
}
],
"kind": "svn",
"revisions": [
{
"module": "repo_url",
"revision": 8953
},
{
"module": "repo_url",
"revision": 9032
}
]
},
"culprits": [
{
"absoluteUrl": "http://localhost:8080/user/username",
"fullName": "username"
}
]
}
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
return jsonify({'tasks': tasks})

if name == 'main':
app.run(debug=True)