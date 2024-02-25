from flask import request
from flask_restful import Resource
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController
from core.factory import factoryApp
from core.response import error_response
factory_app = factoryApp()


class WebhookRegisterApi(Resource):
    @error_response
    def post(self):
        try:
            req = WebhookRegisterRequest(**request.json)
        except Exception as e:
            raise e

        try:
            registerWebhookController(factory_app, req)
        except Exception as e:
            factory_app.session.rollback()
            raise e
        
        return {"message": "ok"}, 200
