from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class App_Context(object):
    def __init__(self) -> None:
        self.session = None 
    

    def get_session_local(DATABASE_URL: str) -> sessionmaker:
        engine = create_engine(DATABASE_URL)
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)