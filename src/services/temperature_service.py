from src.services.formula_factory import FormulaFactory

legal_units = ["f", "c", "k", "r"]

factory = FormulaFactory()


def get_converted_temperature(my_input, my_output, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in legal_units or to_unit not in legal_units:
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


def is_a_number(num):
    num = num.replace(".", "")
    num = num.replace(",", "")
    return num.isnumeric()