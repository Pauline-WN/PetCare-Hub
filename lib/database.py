from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating an engine to connect to the database
DATABASE_URL = "sqlite:///petcarehub.db"
engine = create_engine(DATABASE_URL)
# creating a workspace whre we can interact with the database.
Session = sessionmaker(bind=engine) 

#the base class for the database models which helps in creating tables.
Base = declarative_base() 

#initializing the database which creates all the tables defined in the models.
def init_db():
    Base.metadata.create_all(engine)
