from flask import Flask, request
from flask_restful import Resource, Api
from app.schema.webhook import WebhookRegisterRequest
from app.controllers.webhook_register import registerWebhookController
from app.core.factory import factoryApp
app = Flask(__name__)
api = Api(app=app)

factory_app = factoryApp()

class Webhook(Resource):
    def post(self):
        try:
            req = WebhookRegisterRequest(**request.json)
        except Exception as e:
            return {
                "errors":e
            },400
        
        try:
            registerWebhookController(factoryApp,req)
        except Exception as e:
            print("")