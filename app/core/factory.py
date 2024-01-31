import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from celery import Celery


class factoryApp(object):
    def __init__(self) -> None:
        self.session = self.get_session_local()
        self.celery = Celery()
        self.upload_file = os.getenv("UPLOAD_FILE")

    def get_session_local(self) -> sessionmaker:
        print("DATABASE_URL ", os.getenv("DATABASE_URL"))
        engine = create_engine(os.getenv("DATABASE_URL"))
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    
    def make_celery(self):
        # Configure Celery. Replace 'your_broker_url' and 'your_backend_url' with actual URLs
        broker_url = os.getenv('CELERY_BROKER_URL', None)
        backend_url = os.getenv('CELERY_RESULT_BACKEND',None)
        celery = Celery('your_app_name', broker=broker_url, backend=backend_url)

        # Additional Celery configuration can go here
        celery.conf.update(task_serializer='json')

        return celery