from app import app
from app import db
from app.models import Event
from flask import jsonify
from flask import request

@app.route('/getEvents', methods = ['GET'])
def getEvents():
    data = {}
    data['events'] = Event.query.all()

    response = jsonify(data)
    response.status_code = 200
    return response 

@app.route('/addEvent', methods = ['POST'])
def addEvent():
    data = {}
    json = request.get_json()
    newEvent = Event(event=json['event'],
                     transactionHash=json['transactionHash'], 
                     blockNumber=json['blockNumber'],
                     date=json['date'])
    db.session.add(newEvent)
    db.session.commit()

    response = jsonify(data)
    response.status_code = 200
    return response 
