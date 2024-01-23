from flask import Flask, request
from flask_restful import Resource, Api
from app.schema.webhook import WebhookRegisterRequest
app = Flask(__name__)
api = Api(app=app)


class Webhook(Resource):
    def post(self):
        try:
            req = WebhookRegisterRequest(**request.json)
        except Exception as e:
            return {
                "errors":e
            },400
        
        