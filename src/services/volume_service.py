from src.services.validation_service import validate_volume, is_a_number
from src.services.volume_factory import VolumeFactory

factory = VolumeFactory()

def get_converted_volume(my_input, my_output, from_unit, to_unit):

    is_valid = validate_volume(my_input, from_unit, to_unit)
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
    my_output = round(my_output, 1)
    answer = round(answer, 1)
    if my_output == answer:
        return "correct"
    else:
        print(f"my_output= {my_output} answer = {answer}")
        return "incorrect"

