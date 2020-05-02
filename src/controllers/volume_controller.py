from src.services.volume_service import VolumeService
from src.utils.global_exception_handler import global_exception


@global_exception
def convert(event, context):
    my_input = event['pathParameters']['input']
    output = event['pathParameters']['output']
    from_unit = event['pathParameters']['from_unit']
    to_unit = event['pathParameters']['to_unit']
    from_unit = from_unit.lower()
    from_unit = from_unit[0]
    to_unit = to_unit.lower()
    to_unit = to_unit[0]
    answer = VolumeService.get_converted_volume(my_input, output, from_unit, to_unit)
    answer = answer.replace("\"", "")
    response = {'statusCode': 200, 'isBase64Encoded': False, 'headers': {}, 'body': answer}
    return response
