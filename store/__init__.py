import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

print('store init!')
root_path = os.path.dirname(sys.modules['__main__'].__file__)
engine = create_engine(f'sqlite:///{root_path}\\leadtime.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)