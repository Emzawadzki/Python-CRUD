from flask_api import status


def create_error(error, custom_status):
    return {
        "data": None,
        "error": error,
    }, custom_status


def create_response(data, custom_status=status.HTTP_200_OK):
    return {
        "data": data,
        "error": None,
    }, custom_status
