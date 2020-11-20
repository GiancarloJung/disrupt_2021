import os
import sqlalchemy as db

from app.libs.singleton.singleton_meta import SingletonMeta

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()

class Database(metaclass=SingletonMeta):
    engine = db.create_engine(os.environ['DATABASE_URL'])
    session = None

    def __init__(self):
        self.session = scoped_session(sessionmaker(bind=self.engine))
        self.connection = self.engine.connect()
        Base.metadata.create_all(self.engine)

        print(f'{self}: DB Instance Created')
