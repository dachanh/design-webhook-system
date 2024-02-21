from flask import request
from flask_restful import Resource
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController
from core.factory import factoryApp
from core.response import error_response
factory_app = factoryApp()

class UploadFile(Resource):
    @error_response
    def post(self, user_ID):
            if 'file' not in request.files:
                return {'message': 'No file part'}, 400
            file = request.files['file']
            