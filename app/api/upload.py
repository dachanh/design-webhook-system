from flask import request
from flask_restful import Resource
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController
from core.factory import factoryApp
from core.response import error_response
factory_app = factoryApp()


class UploadFileEvent(Resource):
     @error_response
     def post(self):
          