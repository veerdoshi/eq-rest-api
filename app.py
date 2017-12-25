import os

from flask import Flask
from flask_restful import Api

from resources.quake import Quake, QuakeList
from resources.sensor import Sensor, SensorList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'veer'
api = Api(app)


api.add_resource(Sensor, '/sensor/<string:name>')
api.add_resource(Quake, '/quake')

api.add_resource(QuakeList, '/quakes')
api.add_resource(SensorList, '/sensors')
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
