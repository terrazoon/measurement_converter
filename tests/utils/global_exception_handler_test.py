import unittest

from src.controllers import temperature_controller, volume_controller


class GlobalExceptionHandlerTest(unittest.TestCase):

    def test_temperature_exception(self):
        response = temperature_controller.convert(None, None)
        assert response['statusCode'] == 500
        event = {}
        path_parameters = {'input': 32, 'output': 0, 'from_unit': 'Fahrenheit', 'to_unit': 'Celsius'}
        event['pathParameters'] = path_parameters
        response = temperature_controller.convert(event, None)
        assert response['statusCode'] == 200

    def test_volume_exception(self):
        response = volume_controller.convert(None, None)
        assert response['statusCode'] == 500
        event = {}
        path_parameters = {'input': 1, 'output': 16, 'from_unit': 'Gallons', 'to_unit': 'Cups'}
        event['pathParameters'] = path_parameters
        response = volume_controller.convert(event, None)
        assert response['statusCode'] == 200
