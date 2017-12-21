from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('magnitude',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    @jwt_required()
    def get(self, measure):
        quakeitem = ItemModel.find_by_measure(measure)
        if quakeitem:
            return quakeitem.json()
        return {'message': 'Quake measure not found'}, 404

    def post(self, name):
        data = Item.parser.parse_args()
        quakeitem = ItemModel(measure, **data)
        quakeitem.save_to_db()
        return quakeitem.json(), 201

class ItemList(Resource):
    def get(self):
         return {'quakes': [quakeitem.json() for quakeitem in ItemModel.query.all()]}
