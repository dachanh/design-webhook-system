import logging
from flask import Flask
from flask_restful import Api
from api.webhook import WebhookRegisterApi
from api.upload import UploadFileAPI
from api.event_type import EventTypeAPI

app = Flask(__name__)

if not app.debug:
    app.logger.setLevel(logging.INFO)  # Set the logging level

    # StreamHandler logs to stderr by default
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


def route_webhook():
    webhook_api = Api(app=app)
    webhook_api.add_resource(WebhookRegisterApi, "/webhook/register")


def route_upload_file():
    upload_file_api = Api(app=app)
    upload_file_api.add_resource(UploadFileAPI, "/upload_file/webhook_id/<webhook_id>")


def route_event_type():
    event_type_api = Api(app=app)
    event_type_api.add_resource(EventTypeAPI, "/event_type")


route_webhook()
route_upload_file()
route_event_type()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082, debug=True)
