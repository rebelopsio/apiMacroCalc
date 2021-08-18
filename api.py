from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from results import SetMacros, Results

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sex', type=str)
parser.add_argument('weight', type=int)
parser.add_argument('heightinches', type=int)
parser.add_argument('age', type=int)


class apiMacroCalc(Resource):

    def get(self):
        req_data = {}
        args = parser.parse_args()
        req_data['sex'] = args['sex']
        req_data['weight'] = args['weight']
        req_data['height_inches'] = args['heightinches']
        req_data['age'] = args['age']
        return req_data, 201


api.add_resource(apiMacroCalc, '/')

if __name__ == '__main__':
    app.run(debug=True)
