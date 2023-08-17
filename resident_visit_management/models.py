from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Resident(Base):
    __tablename__ = 'residents'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)
    visits = relationship('Visit', backref='resident')

    def __init__(self, id: int, name: str, phone_number: str, email: str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email

class Visitor(Base):
    __tablename__ = 'visitors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    nic = Column(String)
    vehicle_number = Column(String)
    visits = relationship('Visit', backref='visitor')

    def __init__(self, id: int, name: str, phone_number: str, nic: str, vehicle_number: str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.nic = nic
        self.vehicle_number = vehicle_number

class Visit(Base):
    __tablename__ = 'visits'
    
    id = Column(Integer, primary_key=True)
    scheduled_time = Column(DateTime, default=datetime.utcnow)
    is_approved = Column(Boolean, default=False)
    resident_id = Column(Integer, ForeignKey('residents.id'))
    visitor_id = Column(Integer, ForeignKey('visitors.id'))

    def __init__(self, id: int, scheduled_time: datetime, is_approved: bool, resident: Resident, visitor: Visitor):
        self.id = id
        self.scheduled_time = scheduled_time
        self.is_approved = is_approved
        self.resident = resident
        self.visitor = visitor

class Security(Base):
    __tablename__ = 'security'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
