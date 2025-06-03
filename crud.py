from sqlalchemy.orm import Session
from models import Users, Notes, Tags
from schemas import UsersSchema, NotesSchema, TagsSchema

# retrieve a new user to the database using id
def get_user_by_id(db: Session, user_id: int):  
    return db.query(Users).filter(Users.id == user_id).first()  


# a new user is added to the database
def add_user_to_db(db: Session, new_user: Users):
    user_instance = Users(**new_user.dict())  
    db.add(user_instance)                    
    db.commit()                               
    db.refresh(user_instance)                 #
    return user_instance


# ensures success retrieval of notes
def fetch_notes(db: Session, offset: int = 0, max_results: int = 10):
    notes_list = db.query(Notes).offset(offset).limit(max_results).all()  # Paginated fetch
    return notes_list


# Create a new note and associate it with a user and tags
def add_note(db: Session, note_data: Notes, owner_id: int):
    
    note_entry = Notes(
        title=note_data.title,
        content=note_data.content,
        is_archived=note_data.is_archived,
        user_id=owner_id
    )

    # the notes are associated to the tags
    for tag_label in note_data.tags:
        existing_tag = db.query(Tags).filter(Tags.name == tag_label).first()
        if not existing_tag:
            existing_tag = Tags(name=tag_label)
        note_entry.tags.append(existing_tag)

#add note and commit changes to the session
    db.add(note_entry)        
    db.commit()               
    db.refresh(note_entry)   
    return note_entry         