from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import pandas as pd

# Load the .env file variables
load_dotenv()


def db_connect():
    # Retrieve the DATABASE_URL from environment variables
    database_url = os.getenv('DATABASE_URL')
    
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set. Please check your .env file.")
    
    try:
        engine = create_engine(database_url)
        engine.connect()
        print("✅ Successfully connected to the database!")
        return engine
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")
        raise
