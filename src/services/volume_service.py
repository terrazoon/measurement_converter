from src.services.validation_constants import ValidationConstants
from src.services.validation_service import ValidationService
from src.services.volume_factory import VolumeFactory

factory = VolumeFactory()


class VolumeService:

    @staticmethod
    def get_converted_volume(my_input, my_output, from_unit, to_unit):
        """
        This method converts a volume from one unit of measurement to another and checks the student's answer.

        It will return "invalid" in the case where the teacher appears to have made a typo.  Otherwise, it will
        return correct or incorrect based on the student's answer
        :param my_input: The original measurement
        :param my_output: the student's answer for the converted measurement
        :param from_unit: the original unit of measurement
        :param to_unit: the new unit of measurement
        :return: "invalid", "correct", or "incorrect"
        """
        from_unit = VolumeService._adjust_units(from_unit)
        to_unit = VolumeService._adjust_units(to_unit)
        is_valid = ValidationService.validate_volume(my_input, from_unit, to_unit)
        if not is_valid:
            return ValidationConstants.INVALID

        if not ValidationService.is_a_number(my_output):
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

    @staticmethod
    def _adjust_units(unit_str):
        """
        This is a convenience method to assist teachers who are power users.
        Instead of typing Fahrenheit or Rankine over and over, they can type 'f' and 'r' instead.
        But we have to handle the case of cubic-feet and cubic-inches so the abbreviations are unique
        :param unit_str: the original unit
        :return: the abbreviation
        """
        if unit_str == 'cubic_inches' or unit_str == 'cubic-inches':
            unit_str = 'i'
        elif unit_str == 'cubic_feet' or unit_str == 'cubic-feet':
            unit_str = 'f'
        return unit_str
