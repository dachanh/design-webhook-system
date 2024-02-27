from typing import *
import traceback
from flask import current_app as app


def generate_response(
    message: str, data: dict = {}, error: bool = False, code: int = 200
):
    return {"message": message, "data": data, "error": error}, code


def error_response(function):
    def exception_handler(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as exc:
            app.logger.error(repr(exc))  # Log the exception
            app.logger.error(traceback.format_exc())  # Log the traceback
            messageRaw = str(repr(exc))

            return generate_response(
                message=messageRaw.replace("Exception('", "")
                .replace("')", "")
                .replace('Exception("', "")
                .replace('")', ""),
                error=True,
                code=400,
            )

    return exception_handler
