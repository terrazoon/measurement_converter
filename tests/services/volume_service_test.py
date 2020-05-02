import unittest

from src.services.validation_constants import ValidationConstants
from src.services.volume_service import VolumeService

test_list = [
    [25.6, 6.1, 'c', 'l', ValidationConstants.CORRECT],
    [6.0567, 25.6, 'l', 'c', ValidationConstants.CORRECT],
    [16, 1, 'c', 'g', ValidationConstants.CORRECT],
    [1, 16, 'g', 'c', ValidationConstants.CORRECT],
    [1, 1728, 'f', 'i', ValidationConstants.CORRECT],
    [1728, 1, 'i', 'f', ValidationConstants.CORRECT],
    [1, 16, 'c', 't', ValidationConstants.CORRECT],
    [16, 1, 't', 'c', ValidationConstants.CORRECT],
    [1, 119.7, 'f', 'c', ValidationConstants.CORRECT],
    [119.7, 1, 'c', 'f', ValidationConstants.CORRECT],
    [14.438, 1, 'i', 'c', ValidationConstants.CORRECT],
    [1, 14.438, 'c', 'i', ValidationConstants.CORRECT],
    [1, 256, 'g', 't', ValidationConstants.CORRECT],
    [256, 1, 't', 'g', ValidationConstants.CORRECT],
    [1, 1915.01, 'f', 't', ValidationConstants.CORRECT],
    [1915.01, 1, 't', 'f', ValidationConstants.CORRECT],
    [1, 1.10823, 'i', 't', ValidationConstants.CORRECT],
    [1.10823, 1, 't', 'i', ValidationConstants.CORRECT],
    [7.48052, 1, 'g', 'f', ValidationConstants.CORRECT],
    [1, 7.48052, 'f', 'g', ValidationConstants.CORRECT],
    [1, 231, 'g', 'i', ValidationConstants.CORRECT],
    [231, 1, 'i', 'g', ValidationConstants.CORRECT],
    [4, 4, 'i', 'g', ValidationConstants.INCORRECT],
    [1, 12, 'f', 't', ValidationConstants.INCORRECT],
    [1, 2, 'y', 'z', ValidationConstants.INVALID],
    ['dog', 1, 'f', 'i', ValidationConstants.INVALID],
    [1, 'dog', 'f', 'i', ValidationConstants.INCORRECT],
    ['1', '231', 'g', 'i', ValidationConstants.CORRECT],
    [1, 67.628, 'l', 't', ValidationConstants.CORRECT],
    [67.628, 1, 't', 'l', ValidationConstants.CORRECT],
    [1, 61.028, 'l', 'i', ValidationConstants.CORRECT],
    [61.028, 1, 'i', 'l', ValidationConstants.CORRECT],
    [1, 0.0353147, 'l', 'f', ValidationConstants.CORRECT],
    [0.0353147, 1, 'f', 'l', ValidationConstants.CORRECT],
    [1, 1, 'f', 'f', ValidationConstants.CORRECT],
    [1, 2, 'f', 'f', ValidationConstants.INCORRECT],
    [1, 1, 'f', 'z', ValidationConstants.INVALID],
    [1, 1, 'cubic-feet', 'cubic-feet', ValidationConstants.CORRECT],
    [1, 1, 'cubic-inches', 'cubic-inches', ValidationConstants.CORRECT],
    [73.12, 19.4, 'gallons', 'kelvin', ValidationConstants.INVALID]
]


class VolumeServiceTest(unittest.TestCase):

    def test_volume_conversions(self):
        for test in test_list:
            result = VolumeService.get_converted_volume(test[0], test[1], test[2], test[3])
            if result != test[4]:
                print(f"{result} {test}")
            assert result == test[4]
