# design-webhook-system


![API Webhook Registration Process](document/webhook_register.svg)

the sequence of interactions for registering a webhook could be as follows:
- The User Application sends a registration request to the Webhook Registration API.
- The Webhook Registration API forwards this request to the Webhook Service.
- The Webhook Service validates the request and registers the endpoint in the Database.
- The Database acknowledges the registration.
- The Webhook Service sends a confirmation response back to the User Application.

![ File Upload and Webhook Notification Process](document/file_upload.svg)

- User Application: The external application where the user initiates the file upload.
- Upload Service: A Python-based service that handles file uploads.
- Task Queue (Celery): Manages asynchronous tasks, such as processing the file upload.
- Webhook Service: Notifies the User Application via a webhook when the upload is successfully completed.


![Database](document/database.svg)