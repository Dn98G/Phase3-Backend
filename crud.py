from sqlalchemy.orm import Session
from models import User, Note, Tag
from schemas import NoteCreate, UserCreate

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: NoteCreate, user_id: int):
    db_note = Note(
        title=note.title,
        content=note.content,
        is_archived=note.is_archived,
        user_id=user_id
    )

    for tag_name in note.tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
        db_note.tags.append(tag)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note