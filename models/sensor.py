from db import db

class SensorModel(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Integer(80))

    quakes = db.relationship('QuakeModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'magnitude': self.magnitude, 'quakes': [quake.json() for quake in self.quakes.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()