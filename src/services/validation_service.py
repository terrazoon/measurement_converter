valid_volumes = ['c', 'f', 'g', 'i', 'l', 't']
valid_temperature_scales = ["f", "c", "k", "r"]


def validate_volume(my_input, from_units, to_units):
    if not is_a_number(my_input) and not is_a_number(my_input):
        return False
    first_letter_from = from_units.lower()[0]
    if first_letter_from not in valid_volumes:
        return False
    first_letter_to = to_units.lower()[0]
    if first_letter_to not in valid_volumes:
        return False
    return True


def validate_temperature(my_input, from_units, to_units):
    if not is_a_number(my_input) and not is_a_number(my_input):
        return False
    first_letter_from = from_units.lower()[0]
    if first_letter_from not in valid_temperature_scales:
        return False
    first_letter_to = to_units.lower()[0]
    if first_letter_to not in valid_temperature_scales:
        return False
    return True


def is_a_number(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return True

    num = num.replace(".", "")
    num = num.replace(",", "")
    return num.isnumeric()
