import pytz
from sqlalchemy.ext.declarative import declarative_base

tz = pytz.timezone('Europe/Berlin')

Base = declarative_base()
