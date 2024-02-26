import json
from http import HTTPStatus
from typing import *
import traceback

def generate_response(
    message: str,
    data: dict = {},
    error: bool = False,
    code:int = 200
):
    return {"message": message, "data": data, "error": error}, code



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
                code = 400
            )

    return exception_handler