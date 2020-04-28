import unittest

from src.services.temperature_service import get_converted_temperature


class TemperatureServiceTest(unittest.TestCase):
    def test_convert_from_fahrenheit_correct(self):
        result = get_converted_temperature(32, 0.0000, 'f', 'c')
        assert result == "correct"

        result = get_converted_temperature(32, 273.15, 'f', 'k')
        assert result == "correct"

        result = get_converted_temperature(0, 459.67, 'f', 'r')
        assert result == "correct"

        result = get_converted_temperature(84.2, 543.94, 'f', 'r')
        assert result == "correct"

    def test_convert_from_fahrenheit_incorrect(self):
        result = get_converted_temperature(32, 1000.1, 'f', 'c')
        assert result == "incorrect"

        result = get_converted_temperature(6.5, "dog", "f", "r")
        assert result == "incorrect"

    def test_convert_from_fahrenheit_invalid(self):
        result = get_converted_temperature(32, 1000, "f", "z")
        assert result == "invalid"

    def test_convert_strange(self):
        result = get_converted_temperature(32, 32, "f", "f")
        assert result == "correct"

        result = get_converted_temperature(136.1, 45.2, "dog", "c")
        assert result == "invalid"

    def test_convert_from_kelvin_to_fahrenheit(self):
        result = get_converted_temperature(317.33, 111.554, "k", "f")
        assert result == "incorrect"

    def test_convert_from_rankine_to_kelvin(self):
        result = get_converted_temperature(900, 500, "r", "k")
        assert result == "correct"
