import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class factoryApp(object):
    def __init__(self) -> None:
        self.session = self.get_session_local()
    

    def get_session_local(self) -> sessionmaker:
        engine = create_engine(os.getenv("DATABASE_URL"))
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)()