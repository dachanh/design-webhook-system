from flask import Flask
from flask_restful import Api
from api.webhook import WebhookRegister

app = Flask(__name__)


def route_webhook():
    webhook_api = Api(app=app)
    webhook_api.add_resource(WebhookRegister, "/webhook/register")


if __name__ == "__main__":
    route_webhook()
    app.run(host="0.0.0.0", port=8081, debug=True)
