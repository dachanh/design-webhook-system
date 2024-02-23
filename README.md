# design-webhook-system

## Sequence API Webhook Registration Process

![API Webhook Registration Process](document/webhook_register.svg)

the sequence of interactions for registering a webhook could be as follows:
- The User Application sends a registration request to the Webhook Registration API.
- The Webhook Registration API forwards this request to the Webhook Service.
- The Webhook Service validates the request and registers the endpoint in the Database.
- The Database acknowledges the registration.
- The Webhook Service sends a confirmation response back to the User Application.

## Sequence File Upload and Webhook Notification Process

![ File Upload and Webhook Notification Process](document/file_upload.svg)

The sequence of interactions could be as follows:
- User Application: The external application where the user initiates the file upload.
- Upload Service: A Python-based service that handles file uploads.
- Task Queue (Celery): Manages asynchronous tasks, such as processing the file upload.
- Webhook Service: Notifies the User Application via a webhook when the upload is successfully completed.

## Database

![Database](document/database.svg)