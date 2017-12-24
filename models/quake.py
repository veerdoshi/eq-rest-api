from db import db

class QuakeModel(db.Model):
    __tablename__ = 'quakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float(precision=1))
    latitude = db.Column(db.Float(precision=4))
    longitude = db.Column(db.Float(precision=4))

    sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.id'))
    sensor = db.relationship('SensorModel')

    def __init__(self, magnitude, latitude, longitude, sensor_id):
        self.magnitude = magnitude
        self.latitude = latitude
        self.longitude = longitude
        self.sensor_id = sensor_id

    def json(self):
        return {'magnitude': self.magnitude, 'latitude': self.latitude, 'longitude': self.longitude}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
