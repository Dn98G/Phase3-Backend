from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Float, Text, ForeignKey, Table, Boolean, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

#this section conects the db
engine = create_engine('sqlite:///noteapp.db', echo=True)

#create a session in this section
Session = sessionmaker(bind=engine)

Base = declarative_base()

note_tags = Table(
    'note_tags',
    Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    notes = relationship('Note', back_populates='user')

    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    is_archived = Column(Boolean, default=False)

    user = relationship('User', back_populates='notes')
    tags = relationship('Tag', secondary=note_tags, back_populates='notes')

    def __repr__(self):
        return f"<Note(title='{self.title}', user_id={self.user_id})>"

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    notes = relationship('Note', secondary=note_tags, back_populates='tags')

    def __repr__(self):
        return f"<Tag(name='{self.name}')>"