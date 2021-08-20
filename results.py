from datetime import datetime
from json import JSONEncoder


class SetMacros:
    def __init__(self, calories=0, protein=0, carbs=0, fats=0) -> None:
        self._calories = calories
        self._protein = protein
        self._carbs = carbs
        self._fats = fats

    def get_calories(self) -> int:
        return self._calories

    def get_protein(self) -> int:
        return self._protein

    def get_carbs(self) -> int:
        return self._carbs

    def get_fats(self) -> int:
        return self._fats

    def set_calories(self, calories: int) -> None:
        self._calories = calories

    def set_protein(self, protein: int) -> None:
        self._protein = protein

    def set_carbs(self, carbs: int) -> None:
        self._carbs = carbs

    def set_fats(self, fats: int) -> None:
        self._fats = fats


class Results:
    def __init__(self, basal_metabolic_rate=0):
        self._basal_metabolic_rate = basal_metabolic_rate
        self._created_date = datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
    
    def get_created_date(self) -> datetime:
        return self._created_date
    
    def get_basal_metabolic_rate(self) -> int:
        return self._basal_metabolic_rate
    
    def set_basal_metabolic_rate(self, basal_metabolic_rate:int) -> None:
        self._basal_metabolic_rate = basal_metabolic_rate

    rest_day_macros = SetMacros()
    light_day_macros = SetMacros()
    moderate_day_macros = SetMacros()
    hard_day_macros = SetMacros()

class ResultsEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Results):
            return object.__dict__
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return JSONEncoder.default(self, object)