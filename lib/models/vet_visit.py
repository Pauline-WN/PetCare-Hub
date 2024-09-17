from sqlalchemy import Column, Integer, String, Date, ForeignKey
from lib.database import Base

class VetVisit(Base):
    __tablename__ = 'vet_visits'
    
    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'))
    visit_date = Column(Date, nullable=False)
    reason = Column(String, nullable=False)
    vet_name = Column(String)
