from utils import db_connect
engine = db_connect()

# your code here
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now import db_connect
from utils import db_connect

# Connect to the database
engine = db_connect()
