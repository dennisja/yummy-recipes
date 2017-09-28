from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(80)),
    created = db.Column(db.DateTime)

    def __init__(self, first_name,last_name,email,password, created=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        if not created:
            self.created = datetime.utcnow()
        else:
            self.created = created
    
    def __repr__(self):
        return "<User {} {}>".format(self.first_name,self.last_name)
