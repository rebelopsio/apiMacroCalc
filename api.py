from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from results import ResultsEncoder, SetMacros, Results
from calculations import Calculations
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sex', type=str)
parser.add_argument('weight', type=int)
parser.add_argument('heightinches', type=int)
parser.add_argument('age', type=int)


class apiMacroCalc(Resource):

    def get(self):
        args = parser.parse_args()
        sex = args['sex']
        weight = args['weight']
        height = args['heightinches']
        age = args['age']

        bMR = round(Calculations.basal_metabolic_rate(
            sex, age, height, weight))
        rest_day_calories = round(Calculations.caloric_intake(bMR, "rest"))
        light_day_calories = round(Calculations.caloric_intake(bMR, "light"))
        moderate_day_calories = round(
            Calculations.caloric_intake(bMR, "moderate"))
        hard_day_calories = round(Calculations.caloric_intake(bMR, "hard"))

        obj_rest_day_macros = Calculations.create_macros(
            rest_day_calories, weight, "rest")
        obj_light_day_macros = Calculations.create_macros(
            light_day_calories, weight, "light")
        obj_moderate_day_macros = Calculations.create_macros(
            moderate_day_calories, weight, "moderate")
        obj_hard_day_macros = Calculations.create_macros(
            hard_day_calories, weight, "hard")

        macros = Results()
        macros.rest_day_macros.set_protein(obj_rest_day_macros.protein)
        macros.rest_day_macros.set_carbs(obj_rest_day_macros.carbs)
        macros.rest_day_macros.set_fats(obj_rest_day_macros.fats)
        macros.rest_day_macros.set_calories(obj_rest_day_macros.tdee)
        macros.light_day_macros.set_protein(obj_light_day_macros.protein)
        macros.light_day_macros.set_carbs(obj_light_day_macros.carbs)
        macros.light_day_macros.set_fats(obj_light_day_macros.fats)
        macros.light_day_macros.set_calories(obj_light_day_macros.tdee)
        macros.moderate_day_macros.set_protein(obj_moderate_day_macros.protein)
        macros.moderate_day_macros.set_carbs(obj_moderate_day_macros.carbs)
        macros.moderate_day_macros.set_fats(obj_moderate_day_macros.fats)
        macros.moderate_day_macros.set_calories(obj_moderate_day_macros.tdee)
        macros.hard_day_macros.set_protein(obj_hard_day_macros.protein)
        macros.hard_day_macros.set_carbs(obj_hard_day_macros.carbs)
        macros.hard_day_macros.set_fats(obj_hard_day_macros.fats)
        macros.hard_day_macros.set_calories(obj_hard_day_macros.tdee)
        macros.set_basal_metabolic_rate(bMR)

        json_data = ResultsEncoder().encode(macros)
        return json_data, 201


api.add_resource(apiMacroCalc, '/')

if __name__ == '__main__':
    app.run(debug=True)
