import unittest

from src.services.volume_service import VolumeService

test_list = [
    [25.6, 6.1, 'c', 'l', 'correct'],
    [6.0567, 25.6, 'l', 'c', 'correct'],
    [16, 1, 'c', 'g', 'correct'],
    [1, 16, 'g', 'c', 'correct'],
    [1, 1728, 'f', 'i', 'correct'],
    [1728, 1, 'i', 'f', 'correct'],
    [1, 16, 'c', 't', 'correct'],
    [16, 1, 't', 'c', 'correct'],
    [1, 119.7, 'f', 'c', 'correct'],
    [119.7, 1, 'c', 'f', 'correct'],
    [14.438, 1, 'i', 'c', 'correct'],
    [1, 14.438, 'c', 'i', 'correct'],
    [1, 256, 'g', 't', 'correct'],
    [256, 1, 't', 'g', 'correct'],
    [1, 1915.01, 'f', 't', 'correct'],
    [1915.01, 1, 't', 'f', 'correct'],
    [1, 1.10823, 'i', 't', 'correct'],
    [1.10823, 1, 't', 'i', 'correct'],
    [7.48052, 1, 'g', 'f', 'correct'],
    [1, 7.48052, 'f', 'g', 'correct'],
    [1, 231, 'g', 'i', 'correct'],
    [231, 1, 'i', 'g', 'correct'],
    [4, 4, 'i', 'g', 'incorrect'],
    [1, 12, 'f', 't', 'incorrect'],
    [1, 2, 'y', 'z', 'invalid'],
    ['dog', 1, 'f', 'i', 'invalid'],
    [1, 'dog', 'f', 'i', 'incorrect'],
    ['1', '231', 'g', 'i', 'correct'],
    [1, 67.628, 'l', 't', 'correct'],
    [67.628, 1, 't', 'l', 'correct'],
    [1, 61.028, 'l', 'i', 'correct'],
    [61.028, 1, 'i', 'l', 'correct'],
    [1, 0.0353147, 'l', 'f', 'correct'],
    [0.0353147, 1, 'f', 'l', 'correct'],
    [1, 1, 'f', 'f', 'correct'],
    [1, 2, 'f', 'f', 'incorrect'],
    [1, 1, 'f', 'z', 'invalid'],
    [1, 1, 'cubic-feet', 'cubic-feet', 'correct'],
    [1, 1, 'cubic-inches', 'cubic-inches', 'correct'],
    [73.12, 19.4, 'gallons', 'kelvin', 'invalid']
]


class VolumeServiceTest(unittest.TestCase):

    def test_volume_conversions(self):
        for test in test_list:
            result = VolumeService.get_converted_volume(test[0], test[1], test[2], test[3])
            assert result == test[4]
