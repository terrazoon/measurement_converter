from src.services.validation_constants import ValidationConstants
from src.services.validation_service import validate_volume, is_a_number
from src.services.volume_factory import VolumeFactory

factory = VolumeFactory()


def get_converted_volume(my_input, my_output, from_unit, to_unit):
    from_unit = _adjust_units(from_unit)
    to_unit = _adjust_units(to_unit)

    is_valid = validate_volume(my_input, from_unit, to_unit)
    if not is_valid:
        return ValidationConstants.INVALID

    if not is_a_number(my_input) or not is_a_number(my_output):
        return ValidationConstants.INCORRECT
    my_input = float(my_input)
    my_output = float(my_output)
    if from_unit == to_unit:
        if my_input == my_output:
            return ValidationConstants.CORRECT
        else:
            return ValidationConstants.INCORRECT

    formula = factory.get_formula(from_unit, to_unit)
    answer = formula(my_input)
    my_output = round(my_output, 1)
    answer = round(answer, 1)
    if my_output == answer:
        return ValidationConstants.CORRECT
    else:
        return ValidationConstants.INCORRECT


def _adjust_units(unit_str):
    if unit_str == 'cubic_inches' or unit_str == 'cubic-inches':
        unit_str = 'i'
    elif unit_str == 'cubic_feet' or unit_str == 'cubic-feet':
        unit_str = 'f'
    return unit_str
