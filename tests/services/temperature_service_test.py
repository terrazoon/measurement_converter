import unittest

from src.services.temperature_service import convert_from_fahrenheit


class TemperatureServiceTest(unittest.TestCase):
    def test_convert_from_fahrenheit_correct(self):
        result = convert_from_fahrenheit(32, 0.0000, 'c')
        assert result == "correct"

        result = convert_from_fahrenheit(32, 273.15, 'k')
        assert result == "correct"

        result = convert_from_fahrenheit(0, 459.67, 'r')
        assert result == "correct"

        result = convert_from_fahrenheit(84.2, 543.94, 'r')
        assert result == "correct"

    def test_convert_from_fahrenheit_incorrect(self):
        result = convert_from_fahrenheit(32, 1000.1, 'c')
        assert result == "incorrect"

        result = convert_from_fahrenheit(6.5, "dog", "r")
        assert result == "incorrect"

    def test_convert_from_fahrenheit_invalid(self):
        result = convert_from_fahrenheit(32, 1000, 'z')
        assert result == "invalid"

