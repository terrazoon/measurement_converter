import json

from src.services.volume_service import VolumeService
from src.utils.global_exception_handler import global_exception


@global_exception
def convert(event, context):
    my_input = event['pathParameters']['input']
    output = event['pathParameters']['output']
    from_unit = event['pathParameters']['from_unit']
    to_unit = event['pathParameters']['to_unit']
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    answer = VolumeService.get_converted_volume(my_input, output, from_unit, to_unit)
    answer = answer.replace("\"", "")
    response = {'statusCode': 200,
                'isBase64Encoded': False,
                'headers': {"Access-Control-Allow-Origin": "*"},
                'body': json.dumps(answer)
                }
    return response
