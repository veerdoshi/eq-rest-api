from db import db

class ItemModel(db.Model):
    __tablename__ = 'quakeitems'

    magnitude = db.Column(db.Float(precision=1))
    measure = db.Column(dd.Integer, primary_key=True)

#    location = db.Column(db.String(80), db.ForeignKey('locations.id'))
#    locations = db.relationship('StoreModel')

#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(80))
#    price = db.Column(db.Float(precision=2))

#    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
#    store = db.relationship('StoreModel')

#    def __init__(self, name, price, store_id):
    def __init__(self, magnitude):
        self.magnitude = magnitude
        self.measure = measure

#        self.location = location
#        self.location = location
#
#        self.name = name
#        self.price = price
#        self.store_id = store_id
    def json(self):
#        return {'name': self.name, 'price': self.price}
        return {'measure': self.measure, 'magnitude': self.magnitude}

    @classmethod
    def find_by_measure(cls, name):
        return cls.query.filter_by(measure=measure).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
