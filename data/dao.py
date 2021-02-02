import os
import sys

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

root_path = os.path.dirname(sys.modules['__main__'].__file__)
engine = create_engine(f'sqlite:///{root_path}\\leadtime.sqlite')
Session = sessionmaker(bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)


class WorkType(Base):
    __tablename__ = 'WORK_TYPE'
    rowid = Column(Integer, primary_key=True)
    title = Column(String)


class TShirt(Base):
    __tablename__ = 'TSHIRT'
    rowid = Column(Integer, primary_key=True)
    title = Column(String)


class RWI(Base):
    __tablename__ = 'RWI'
    rowid = Column(Integer, primary_key=True)
    title = Column(String)
    comment = Column(String)
    is_plan = Column(Boolean, default=False)
    work_type = Column(Integer, ForeignKey('WORK_TYPE.rowid'))
    work_type_obj = relationship(WorkType)
    tshirt = Column(Integer, ForeignKey('TSHIRT.rowid'))
    tshirt_obj = relationship(TShirt)
    id = Column(String)
    master = Column(Integer, ForeignKey('RWI.rowid'))
    master_obj = relationship(__tablename__)
