import unittest

from src.services.temperature_service import get_converted_temperature


class TemperatureServiceTest(unittest.TestCase):
    test_list = [
        [32, 0.0000, 'f', 'c', 'correct'],
        [0.0000, 32, 'c', 'f', 'correct'],
        [0, 459.67, 'f', 'r', 'correct'],
        [459.67, 0, 'r', 'f', 'correct'],
        [32, 273.15, 'f', 'k', 'correct'],
        [273.15, 32, 'k', 'f', 'correct'],
        [84.2, 543.94, 'f', 'r', 'correct'],
        [32, 1000.1, 'f', 'c', 'incorrect'],
        [6.5, 'dog', 'f', 'r', 'incorrect'],
        [32, 1000, 'f', 'z', 'invalid'],
        [32, 32, 'f', 'f', 'correct'],
        [136.1, 45.2, 'dog', 'c', 'invalid'],
        [317.33, 111.554, 'k', 'f', 'incorrect'],
        [900, 500, 'r', 'k', 'correct']
    ]

    def test_temperature_conversions(self):
        for test in self.test_list:
            result = get_converted_temperature(test[0], test[1], test[2], test[3])
            assert result == test[4]
