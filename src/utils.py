from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from pathlib import Path

# Explicitly specify the .env file path
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

def db_connect():
    # Debugging output
    print("🔍 DATABASE_URL:", os.getenv('DATABASE_URL'))
    
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("❌ DATABASE_URL environment variable is not set. Please check your .env file.")
    
    try:
        engine = create_engine(database_url)
        engine.connect()
        print("✅ Successfully connected to the database!")
        return engine
    except Exception as e:
        print(f"❌ Failed to connect to the database: {e}")
        raise
