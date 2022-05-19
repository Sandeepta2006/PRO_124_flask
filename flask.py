from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        "Contact": "9984628945",
        "Name": "Bruno",
        "done": False
    },
    {
        'id': 2,
        "Contact": "9984628954",
        "Name": "Rodrigo",
        "done": False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }