from flask_restful import Resource, reqparse
from models.quake import QuakeModel

class Quake(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('magnitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    parser = reqparse.RequestParser()
    parser.add_argument('magnitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    parser = reqparse.RequestParser()
    parser.add_argument('latitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    parser = reqparse.RequestParser()
    parser.add_argument('longitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    parser.add_argument('sensor_id',
        type=int,
        required=True,
        help='Every measure needs a sensor id.'
    )

#    @jwt_required()
#    def get(self, name):
#        item = ItemModel.find_by_name(name)
#        if item:
#            return item.json()
#        return {'message': 'Item not found'}, 404


    def post(self):
        data = Item.parser.parse_args()
        quake = QuakeModel(**data)
        try:
            quake.save_to_db()
        except:
            return {"message": "An error occurred while inserting the quake measure"}, 500

        return quake.json(), 201


class QuakeList(Resource):
    def get(self):
         return {'quakes': [quake.json() for quake in QuakeModel.query.all()]}
