class TemperatureFactory:
    formula_map = {}

    def __init__(self):
        self.formula_map = {
            'fc': self.fahrenheit_to_celsius,
            'fk': self.fahrenheit_to_kelvin,
            'fr': self.fahrenheit_to_rankine,
            'cf': self.celsius_to_fahrenheit,
            'ck': self.celsius_to_kelvin,
            'cr': self.celsius_to_rankine,
            'kf': self.kelvin_to_fahrenheit,
            'kc': self.kelvin_to_celsius,
            'kr': self.kelvin_to_rankine,
            'rf': self.rankine_to_fahrenheit,
            'rc': self.rankine_to_celsius,
            'rk': self.rankine_to_kelvin
        }

    def get_formula(self, from_unit, to_unit):
        return self.formula_map[from_unit + to_unit]

    @staticmethod
    def fahrenheit_to_celsius(my_input):
        return (my_input - 32) * 5 / 9

    @staticmethod
    def fahrenheit_to_kelvin(my_input):
        return (my_input - 32) * 5 / 9 + 273.15

    @staticmethod
    def fahrenheit_to_rankine(my_input):
        return my_input + 459.67

    @staticmethod
    def celsius_to_fahrenheit(my_input):
        return (my_input * 9 / 5) + 32

    @staticmethod
    def celsius_to_kelvin(my_input):
        return my_input + 273.15

    @staticmethod
    def celsius_to_rankine(my_input):
        return (my_input * 9 / 5) + 491.67

    @staticmethod
    def kelvin_to_fahrenheit(my_input):
        return (my_input - 273.15) * 9 / 5 + 32

    @staticmethod
    def kelvin_to_celsius(my_input):
        return my_input - 273.15

    @staticmethod
    def kelvin_to_rankine(my_input):
        return my_input * 9 / 5

    @staticmethod
    def rankine_to_fahrenheit(my_input):
        return my_input - 459.67

    @staticmethod
    def rankine_to_celsius(my_input):
        return (my_input - 491.67) * 5 / 9

    @staticmethod
    def rankine_to_kelvin(my_input):
        return my_input * 5 / 9
