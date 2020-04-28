from src.services.formula_factory import FormulaFactory
from src.services.validation_service import validate_temperature, is_a_number

factory = FormulaFactory()


def get_converted_temperature(my_input, my_output, from_unit, to_unit):

    is_valid = validate_temperature(my_input, from_unit, to_unit)
    if not is_valid:
        return "invalid"

    if not is_a_number(my_input) or not is_a_number(my_output):
        return "incorrect"
    my_input = float(my_input)
    my_output = float(my_output)
    if from_unit == to_unit:
        if my_input == my_output:
            return "correct"
        else:
            return "incorrect"

    formula = factory.get_formula(from_unit, to_unit)
    answer = formula(my_input)
    if round(my_output, 1) == round(answer, 1):
        return "correct"
    else:
        return "incorrect"
