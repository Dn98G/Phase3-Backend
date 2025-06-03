from sqlalchemy.orm import Session
from models import Users, Notes, Tags
from schemas import UsersSchema, NotesSchema, TagsSchema


def get_user_by_id(db: Session, username: int):
    return db.query(Users).filter(Users.id == id).first()

def create_user(db: Session, user: Users):
    db_user = Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Notes).offset(skip).limit(limit).all()

def create_note(db: Session, note: Notes, user_id: int):
    db_note = Notes(
        title=note.title,
        content=note.content,
        is_archived=note.is_archived,
        user_id=user_id
    )

    for tag_name in note.tags:
        tag = db.query(Tags).filter(Tags.name == tag_name).first()
        if not tag:
            tag = Tags(name=tag_name)
        db_note.tags.append(tag)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note