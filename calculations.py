from collections import namedtuple


class Calculations:
    @staticmethod
    def basal_metabolic_rate(sex: str, age: int, height_inches: int, weight: int) -> float:
        bmr = 0.0
        if sex.upper() == "MALE":
            bmr = (10 * (weight / 2.2)) + (6.25 * (height_inches * 2.54)
                                           ) - ((5 * age) + 5)  # Mifflin-St. Jeor formula
        elif sex.upper() == "FEMALE":
            bmr = (10 * (weight / 2.2)) + (6.25 * (height_inches * 2.54)
                                           ) - ((5 * age) + 5) - 161  # Mifflin-St. Jeor formula
        return bmr

    @staticmethod
    def caloric_intake(bmr: float, type: str) -> float:
        multiplier = 0.0
        if type == "rest":
            multiplier = 1.2
        elif type == "light":
            multiplier = 1.375
        elif type == "moderate":
            multiplier = 1.55
        elif type == "hard":
            multiplier = 1.725
        calories = bmr * multiplier
        return calories

    @staticmethod
    def create_macros(calories: int, weight: int, type: str) -> namedtuple:
        protein = weight * 1
        carbs = 0

        if type == "rest":
            carbs = round(weight * 0.5)
        elif type == "light":
            carbs = round(weight * 1)
        elif type == "moderate":
            carbs = round(weight * 1.5)
        elif type == "hard":
            carbs = round(weight * 2)

        fats = round((calories - ((carbs + protein) * 4)) / 9)
        if fats < 55:
            fats = 55
        tdee = (protein * 4) + (carbs * 4) + (fats * 9)
        Macros = namedtuple("Macros", "protein carbs fats tdee")
        macros = Macros(protein, carbs, fats, tdee)
        return macros
