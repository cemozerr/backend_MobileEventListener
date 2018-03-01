from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transactionHash = db.Column(db.String(200))
    blockNumber = db.Column(db.Integer)
    event = db.Column(db.String(50))
    date = db.Column(db.String(100))

    def __repr__(self):
        return '<{} Event>'.format(self.event)   
