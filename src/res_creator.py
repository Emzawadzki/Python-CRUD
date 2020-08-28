def create_error(error):
    return {
        "data": None,
        "error": error
    }


def create_response(data):
    return {
        "data": data,
        "error": None
    }
