import unittest

from src.services.temperature_service import TemperatureService
from src.services.validation_constants import ValidationConstants


class TemperatureServiceTest(unittest.TestCase):
    test_list = [
        [32, 0.0000, 'f', 'c', ValidationConstants.CORRECT],
        [0.0000, 32, 'c', 'f', ValidationConstants.CORRECT],
        [0, 459.67, 'f', 'r', ValidationConstants.CORRECT],
        [459.67, 0, 'r', 'f', ValidationConstants.CORRECT],
        [32, 273.15, 'f', 'k', ValidationConstants.CORRECT],
        [273.15, 32, 'k', 'f', ValidationConstants.CORRECT],
        [84.2, 543.94, 'f', 'r', ValidationConstants.CORRECT],
        [32, 1000.1, 'f', 'c', ValidationConstants.INCORRECT],
        [6.5, 'dog', 'f', 'r', ValidationConstants.INCORRECT],
        [32, 1000, 'f', 'z', ValidationConstants.INVALID],
        [32, 32, 'f', 'f', ValidationConstants.CORRECT],
        [136.1, 45.32, 'dog', 'c', ValidationConstants.INVALID],
        [317.33, 111.554, 'k', 'f', ValidationConstants.INCORRECT],
        [900, 500, 'r', 'k', ValidationConstants.CORRECT],
        [0, 273.15, 'c', 'k', ValidationConstants.CORRECT],
        [273.15, 0, 'k', 'c', ValidationConstants.CORRECT],
        [1, 2, 'f', 'f', ValidationConstants.INCORRECT],
        [0, 491.67, 'c', 'r', ValidationConstants.CORRECT],
        [491.67, 0, 'r', 'c', ValidationConstants.CORRECT],
        [500, 900, 'k', 'r', ValidationConstants.CORRECT],
        ['dog', 24, 'k', 'r', ValidationConstants.INVALID],
        [None, 24, 'k', 'r', ValidationConstants.INVALID]

    ]

    def test_temperature_conversions(self):
        for test in self.test_list:
            result = TemperatureService.get_converted_temperature(test[0], test[1], test[2], test[3])
            # if result != test[4]:
            #    print(f" {result} {test}")
            assert result == test[4]
