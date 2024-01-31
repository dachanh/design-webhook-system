import json
from http import HTTPStatus
from typing import *
import traceback


RESPONSE_HEADER = {
    "access-control-allow-origin": "*",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS, POST, PUT",
    "access-control-allow-headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent",
}

HTTP_STATUS_WARNING = 205

def generate_response(
    message: str,
    data: dict = {},
    error: bool = False,
):

    return {"message": message, "data": data, "error": error}



def error_response(function):
    def exception_handler(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as exc:
            print(repr(exc))
            print(traceback.format_exc())
            messageRaw = str(repr(exc))

            return generate_response(
                message=messageRaw.replace("Exception('", "")
                .replace("')", "")
                .replace('Exception("', "")
                .replace('")', ""),
                error=True,
            )

    return exception_handler