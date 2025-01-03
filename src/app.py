import sys
import os
from flask import Flask
from utils import db_connect

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

# Establish database connection
engine = db_connect()

@app.route('/')
def index():
    return "Welcome to the MXN-USD Exchange Rate Predictor!"

if __name__ == "__main__":
    app.run(debug=True)
