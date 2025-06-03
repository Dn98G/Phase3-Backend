from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Float, Text, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

#this section conects the db
engine = create_engine('sqlite:///noteapp.db', echo=True)

#create a session in this section
Session = sessionmaker(bind=engine)

def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)
    address = Column(Integer, nullable=False)
    Visits = relationship("visits", back_populates="users")

class Notes(Base):
    __tablename__ = 'Notes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    title = Column(String(255), nullable=False)
    is_archived = Column(Boolean, default=False)
    Visits = relationship("visits", back_populates="users")

class Tags(Base):
    __tablename__ = 'Tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(Integer, primary_key=False)
    Visits = relationship("visits", back_populates="users")
    

    