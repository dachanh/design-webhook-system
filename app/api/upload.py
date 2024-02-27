from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from celery import chain

from core.factory import factoryApp
from core.response import error_response, generate_response
from tasks.upload_file import UploadFileTask

factory_app = factoryApp()

upload_file_task = UploadFileTask()


class UploadFileAPI(Resource):
    @error_response
    def post(self, webhook_id):
        if "file" not in request.files:
            raise Exception("No file part")
        file = request.files["file"]
        if file.filename == "":
            raise Exception("No selected file")

        if file:
            filename = secure_filename(file.filename)
            # You can now use the user_id in your file processing
            data = {
                "file_content": file.read(),
                "filename": filename,
                "webhook_id": webhook_id,
            }
            task = chain(
                upload_file_task.publish_upload_file.s(data),
                upload_file_task.webhook.s(),
            ).apply_async()

        return generate_response(message="ok")
