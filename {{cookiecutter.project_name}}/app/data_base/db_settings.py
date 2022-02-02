import os
from contextlib import contextmanager

import psycopg2

#production D
from sqlalchemy import create_engine
from finding_buyers.data_base.models import Base
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm
import pandas as pd
from utils import null_to_nan, nan_to_null
from typing import List, Union, Type

POSTGRES_USER = "postgres_leander"
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = "5432"
POSTGRES_DB = "postgres"

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#the engine is to connect to the acutal physical db
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

def load_db_table(table_name:str, **kwargs):
    """
    Loads a database table and turns nans tu nulls
    """
    # here we are getting the relationship between companies and transactions
    table = pd.read_sql_table(
        table_name,
        con=engine, **kwargs)
    table = null_to_nan(table)
    return table

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    try:
        db = psycopg2.connect(f"dbname=postgres user={POSTGRES_USER}"
                              f" host={POSTGRES_HOST} password={POSTGRES_PASSWORD}")
        db.close()
        print(f"connectedd to {POSTGRES_HOST}")
    except Exception as e :
        print(e)
        print("not connected")
