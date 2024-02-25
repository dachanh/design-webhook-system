from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController

from core.factory import factoryApp
from core.response import error_response
from tasks.upload_file import UploadFileTask
factory_app = factoryApp()

upload_file_task = UploadFileTask()

class UploadFileAPI(Resource):
     @error_response
     def post(self,user_id):
        if 'file' not in request.files:
            return {'message': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            return {'message': 'No selected file'}, 400
        
        if file:
            filename = secure_filename(file.filename)
            # You can now use the user_id in your file processing
            data = {
                "file_content":file.read(),
                "filename":filename
            }
            task = upload_file_task.publish_upload_file.apply_async(args=[data])
            print(task.id)
        return{"message": "ok"}, 200
