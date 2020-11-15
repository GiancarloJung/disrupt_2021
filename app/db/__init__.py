import os
import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()

class Database():
    engine = db.create_engine(os.environ['DATABASE_URL'])
    session = None

    def __init__(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))
        self.connection = self.engine.connect()
        Base.metadata.create_all(self.engine)

        print("DB Instance Created")
