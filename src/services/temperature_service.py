from src.services.temperature_factory import TemperatureFactory
from src.services.validation_constants import ValidationConstants
from src.services.validation_service import validate_temperature, is_a_number

factory = TemperatureFactory()


def get_converted_temperature(my_input, my_output, from_unit, to_unit):
    """
        This method converts a temperature from one unit of measurement to another and checks the student's answer.

        It will return "invalid" in the case where the teacher appears to have made a typo.  Otherwise, it will
        return correct or incorrect based on the student's answer
        :param my_input: The original measurement
        :param my_output: the student's answer for the converted measurement
        :param from_unit: the original unit of measurement
        :param to_unit: the new unit of measurement
        :return: "invalid", "correct", or "incorrect"
    """
    is_valid = validate_temperature(my_input, from_unit, to_unit)
    if not is_valid:
        return ValidationConstants.INVALID

    if not is_a_number(my_output):
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
    if round(my_output, 1) == round(answer, 1):
        return ValidationConstants.CORRECT
    else:
        return ValidationConstants.INCORRECT
