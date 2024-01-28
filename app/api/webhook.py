from flask import request
from flask_restful import Resource
from schema.webhook import WebhookRegisterRequest
from controllers.webhook_register import registerWebhookController
from core.factory import factoryApp

factory_app = factoryApp()

class WebhookRegister(Resource):
    def post(self):
        print("--------"*100)
        try:
            req = WebhookRegisterRequest(**request.json)
        except Exception as e:
            print("ERROR :",e)
            return {
                "errors":e
            },400
        print(req)
        try:
            registerWebhookController(factory_app,req)
        except Exception as e:
            print("")
