from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

DATABASE_URL = getenv('DB_URL', '')

engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

class Database:
    def __init__(self):
        self.db = SessionLocal()

    def get_db(self):
        try:
            yield self.db
        finally:
            self.db.close()

db_instance = Database()
