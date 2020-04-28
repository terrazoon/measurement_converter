import json

from src.services.temperature_service import get_converted_temperature


def convert(event, context):
    my_input = event['pathParameters']['input']
    output = event['pathParameters']['output']
    from_unit = event['pathParameters']['from_unit']
    to_unit = event['pathParameters']['to_unit']
    answer = get_converted_temperature(my_input, output, from_unit, to_unit)

    result = {
        "answer": answer
    }

    response = {'isBase64Encoded': False, 'statusCode': 200, 'headers': {}, 'body': json.dumps(result)}
    return response
