class ValidationService:
    VALID_VOLUMES = ['c', 'f', 'g', 'i', 'l', 't']
    VALID_TEMPERATURE_SCALES = ["f", "c", "k", "r"]

    @staticmethod
    def validate_volume(my_input, from_units, to_units):
        return ValidationService._validate(my_input, from_units, to_units, ValidationService.VALID_VOLUMES)

    @staticmethod
    def validate_temperature(my_input, from_units, to_units):
        return ValidationService._validate(my_input, from_units, to_units, ValidationService.VALID_TEMPERATURE_SCALES)

    @staticmethod
    def is_a_number(num):
        if num is None:
            return False
        if isinstance(num, int):
            return True
        if isinstance(num, float):
            return True

        num = num.replace(".", "")
        num = num.replace(",", "")
        return num.isnumeric()

    @staticmethod
    def _validate(my_input, from_units, to_units, valid_list):
        if not ValidationService.is_a_number(my_input):
            return False
        first_letter_from = from_units.lower()[0]
        if first_letter_from not in valid_list:
            return False
        first_letter_to = to_units.lower()[0]
        if first_letter_to not in valid_list:
            return False
        return True
