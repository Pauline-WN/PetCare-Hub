from sqlalchemy import Column, Integer, String, Date, ForeignKey
from lib.database import Base

class CareSchedule(Base):
    __tablename__ = 'care_schedules'
    
    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    task = Column(String, nullable=False)
    frequency = Column(String)
    due_date = Column(Date)
