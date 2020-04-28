import json

from src.services.temperature_service import get_converted_temperature


def convert(event, context):
    my_input = event['pathParameters']['input']
    output = event['pathParameters']['output']
    from_unit = event['pathParameters']['from_unit']
    to_unit = event['pathParameters']['to_unit']
    from_unit = from_unit.lower()
    from_unit = from_unit[0]
    to_unit = to_unit.lower()
    to_unit = to_unit[0]
    answer = get_converted_temperature(my_input, output, from_unit, to_unit)

    result = {
        "answer": answer
    }

    response = {'isBase64Encoded': False, 'statusCode': 200, 'headers': {}, 'body': json.dumps(result)}
    return response
