from flask_restful import Resource
from models.sensor import SensorModel


class Sensor(Resource):
    def get(self, name):
        sensor = SensorModel.find_by_name(name)
        if sensor:
            return sensor.json()
        return {'message': 'Sensor not found'}, 404
    def post(self, name):
        if SensorModel.find_by_name(name):
            return {'message': "A sensor with name '{}' already exists.".format(name)}, 400
        sensor = SensorModel(magnitude)
        try:
            sensor.save_to_db()
        except:
            return {'message': 'An error occurred while creating the sensor.'}, 500

        return sensor.json(), 201

    def delete(self, name):
        sensor = SensorModel.find_by_name(name)
        if sensor:
            sensor.delete_from_db()

            return {'message': 'Sensor deleted'}

class SensorList(Resource):
    def get(self):
        return {'sensors': [sensor.json() for sensor in SensorModel.query.all()]}
