#!/usr/bin/python3
""" lists states hbtn_0e_0_usa """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ lists states hbtn_0e_0_usa """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
