from flask import request
from flask_restful import Resource
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController
from core.factory import factoryApp

factory_app = factoryApp()

class WebhookRegister(Resource):
    def post(self):
        try:
            req = WebhookRegisterRequest(**request.json)
        except Exception as e:
            print("ERROR :",e)
            return {
                "errors":e
            },400

        try:
            registerWebhookController(factory_app,req)
        except Exception as e:
            print(e)
            return {
                "error":e
            },400
        return {
            "message":"ok"
        },200
