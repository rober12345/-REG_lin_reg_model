from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine('postgresql://postgres:ManzanaOrganico1@localhost/reg_lin_reg')
    engine.connect()
    return engine
