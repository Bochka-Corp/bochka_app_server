from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bochka.settings.database import database_settings


class Database:
    def __init__(self):
        self.engine = create_engine(database_settings.get_db_url())

    def get_session(self):
        return sessionmaker(bind=self.engine)


database = Database()
