import logging

logger = logging.getLogger()


def global_exception(func):
    def func_wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            return {'statusCode': 500, 'isBase64Encoded': False, 'headers': {}, 'body': 'Server Error'}

    return func_wrapper
