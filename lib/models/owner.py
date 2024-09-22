from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # Defining relationship with Pet model
    pets = relationship("Pet", back_populates="owner")
