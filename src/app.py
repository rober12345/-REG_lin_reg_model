# your code here
import sys
import os

# Add the parent directory of 'src' to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import db_connect

# Establish database connection
engine = db_connect()
print("✅ Database connection successful!")
