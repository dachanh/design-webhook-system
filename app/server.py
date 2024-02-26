from flask import Flask
from flask_restful import Api
from api.webhook import WebhookRegisterApi
from api.upload import UploadFileAPI

app = Flask(__name__)


def route_webhook():
    webhook_api = Api(app=app)
    webhook_api.add_resource(WebhookRegisterApi, "/webhook/register")


def route_upload_file():
    upload_file_api = Api(app=app)
    upload_file_api.add_resource(UploadFileAPI, "/upload_file/user_id/<user_id>")


route_webhook()
route_upload_file()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
