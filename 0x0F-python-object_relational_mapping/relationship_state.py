#!/usr/bin/python3
""" lists states hbtn_0e_0_usa """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """ lists states hbtn_0e_0_usa """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
