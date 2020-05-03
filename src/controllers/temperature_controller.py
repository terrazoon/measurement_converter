import json

from src.services.temperature_service import TemperatureService
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
    answer = TemperatureService.get_converted_temperature(my_input, output, from_unit, to_unit)
    answer = answer.replace("\"", "")
    response = {'isBase64Encoded': False,
                'statusCode': 200,
                'headers': {"Access-Control-Allow-Origin": "*"},
                'body': json.dumps(answer)
                }
    return response
