# db_test.py

from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DATABASE_URL = "postgresql://app:app@localhost:5432/app"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("✅ Successfully connected to the database!")
except OperationalError as e:
    print("❌ Connection failed:")
    print(e)
