import json


def convert(event, context):
    measurement = event['pathParameters']['amount']
    from_unit = event['pathParameters']['from_unit']
    to_unit = event['pathParameters']['to_unit']

    result = {
        "measurement": measurement,
        "from_unit": from_unit,
        "to_unit": to_unit
    }
    response = {'statusCode': 200, 'isBase64Encoded': False, 'headers': {}, 'body': json.dumps(result)}
    return response
