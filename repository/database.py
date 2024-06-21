from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from time import sleep
from os import getenv

DATABASE_URL = getenv('DB_URL', '')

class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.engine = None
            cls._instance.SessionLocal = None
        return cls._instance

    def initialize(self):
        max_retries = 3
        retry_delay = 5  # seconds
        for retry in range(max_retries):
            try:
                self.engine = create_engine(DATABASE_URL)
                self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
                print("Database connection established.")
                return
            except OperationalError as e:
                print(f"Database connection failed. Retrying in {retry_delay} seconds... (Attempt {retry + 1}/{max_retries})")
                sleep(retry_delay)
        raise Exception("Failed to establish database connection.")

    def get_db(self):
        db = self.SessionLocal()
        try:
            return db
        finally:
            db.close()
    
    def test_connection(self):
        try:
            with self.engine.connect() as connection:
                result = connection.execute(text("SELECT 1=1 "))
                print("Database connection test successful.")
                return True
        except OperationalError as e:
            print(f"Database connection test failed: {e}")
            return False

    def dispose(self):
        if self.engine:
            self.engine.dispose()
            print("Database connection disposed.")

db_manager = DatabaseManager()
db_manager.initialize()
