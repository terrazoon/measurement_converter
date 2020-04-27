import json

from src.exceptions.illegal_temperature_exception import IllegalTemperatureException
from src.exceptions.illegal_temperature_unit_exception import IllegalTemperatureUnitException

legal_units = ["f", "c", "k", "r"]

def get_converted_temperature(input, output, from_unit, to_unit):
    if from_unit.lower() not in legal_units or to_unit.lower() not in legal_units:
        print(f"hitting invalid #1")
        return "invalid"
    if not input.isnumeric() or not output.isnumeric():
        return "incorrect"
    if from_unit == to_unit:
        if input == output:
            return "correct"
        else:
            return "incorrect"
    if from_unit.lower() == "f":
        return convert_from_fahrenheit(input, output, to_unit)
    elif from_unit.lower() == "c":
        return convert_from_celsius(input, output, to_unit)
    elif from_unit.lower() == "k":
        return convert_from_kelvin(input, output, to_unit)
    elif from_unit.lower() == "r":
        return convert_from_rankine(input, output, to_unit)
    else:
        # should not get here, etc.
        return "invalid"

def convert_from_fahrenheit(input, output, to_unit):
    if to_unit.lower() == 'c':
        correct_answer = (input - 32) * 5/9
    elif to_unit.lower() == 'k':
        correct_answer = (input - 32) * 5/9 + 273.15
    elif to_unit.lower() == 'r':
        correct_answer = input + 459.67
    else:
        return "invalid"

    if isinstance(output, str):
        return "incorrect"

    if round(output, 1) == round(correct_answer, 1):
        return "correct"
    else:
        print(f"incorrect input {input} correct_answer = {correct_answer}")
        return "incorrect"

def convert_from_celsius(amount, to_unit):
    pass

def convert_from_kelvin(amount, to_unit):
    pass

def convert_from_rankine(amount, to_unit):
    pass


