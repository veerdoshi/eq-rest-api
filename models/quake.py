from db import db

class QuakeModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    sensor_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    sensor = db.relationship('SensorModel')

    def __init__(self, magnitude, latitude, longitude, sensor_id):
        self.magnitude = magnitude
        self.latitude = latitude
        self.longitude = longitude
        self.sensor_id = sensor_id

#        self.name = name
#        self.price = price
#        self.store_id = store_id
    def json(self):
        return {'magnitude': self.magnitude, 'latitude': self.latitude, 'longitude': self.longitude}

#    @classmethod
#    def find_by_name(cls, name):
#        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
