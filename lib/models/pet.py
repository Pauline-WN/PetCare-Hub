from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.database import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String)
    breed = Column(String)
    age = Column(Integer)

    # Foreign key to link the pet to an owner
    owner_id = Column(Integer, ForeignKey('owners.id'))

    # Defining relationship with Owner model
    owner = relationship("Owner", back_populates="pets")
