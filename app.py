#import the fastapi package here
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import UsersSchema, NotesSchema, TagsSchema
from models import Users, Notes, Tags, get_db
from sqlalchemy.orm import Session

#this initializes it

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])



@app.get("/users/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_db)):
    # Fetch a user by ID
    user = session.query(Users).filter(Users.id == user_id).first()
    return user

@app.post("/users")
def add_user(user: UsersSchema, session: Session = Depends(get_db)):
    # Create a new user using data from UsersSchema
    new_user = Users(**user.model_dump())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)  # Refresh to get the new ID and other defaults
    return {'message': f'User {new_user.id} has been successfully added!'}

@app.patch("/users/{user_id}")
def update_user(user_id: int, user_data: UsersSchema, session: Session = Depends(get_db)):
    # new data is updated to an existing user
    user = session.query(Users).filter(Users.id == user_id).first()
    # the fields provided are updated
    for key, value in user_data.model_dump().items():
        setattr(user, key, value)
    session.commit()
    return {'message': f'User {user_id} successfully updated'}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_db)):
    #removes the user after checking 
    user = session.query(Users).filter(Users.id == user_id).first()
    session.delete(user)
    session.commit()
    return {'message': f'User {user_id} successfully deleted'}

# ====================== NOTES ======================

@app.get("/notes/{notes_id}")
def get_note(notes_id: int, session: Session = Depends(get_db)):
    # checks the notes by use of id
    note = session.query(Notes).filter(Notes.id == notes_id).first()
@app.post("/notes")
def add_note(note: NotesSchema, session: Session = Depends(get_db)):
    # a new note is added
    new_note = Notes(**note.model_dump())
    session.add(new_note)
    session.commit()
    session.refresh(new_note)
    return {'message': f'Note {new_note.id} has been successfully added!'}

@app.patch("/notes/{notes_id}")
def update_note(notes_id: int, note_data: NotesSchema, session: Session = Depends(get_db)):
    # existing note is updated
    note = session.query(Notes).filter(Notes.id == notes_id).first()
    for key, value in note_data.model_dump().items():
        setattr(note, key, value)
    session.commit()
    return {'message': f'Note {notes_id} successfully updated'}

@app.delete("/notes/{notes_id}")
def delete_note(notes_id: int, session: Session = Depends(get_db)):
    # Dnote deleted
    note = session.query(Notes).filter(Notes.id == notes_id).first()
    session.delete(note)
    session.commit()
    return {'message': f'Note {notes_id} successfully deleted'}

# ====================== TAGS ======================

@app.get("/tags/{tag_id}")
def get_tag(tag_id: int, session: Session = Depends(get_db)):
    # a tag is fetched using its ID
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    return tag

@app.post("/tags")
def add_tag(tag: TagsSchema, session: Session = Depends(get_db)):
    # new tag created
    new_tag = Tags(**tag.model_dump())
    session.add(new_tag)
    session.commit()
    session.refresh(new_tag)
    return {'message': f'Tag {new_tag.id} has been successfully added!'}

@app.patch("/tags/{tag_id}")
def update_tag(tag_id: int, tag_data: TagsSchema, session: Session = Depends(get_db)):
    # existing tag is updated
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    for key, value in tag_data.model_dump().items():
        setattr(tag, key, value)
    session.commit()
    return {'message': f'Tag {tag_id} successfully updated'}

@app.delete("/tags/{tag_id}")
def delete_tag(tag_id: int, session: Session = Depends(get_db)):
    # an existing tag gets deleted using its id
    tag = session.query(Tags).filter(Tags.id == tag_id).first()
    session.delete(tag)
    session.commit()
    return {'message': f'Tag {tag_id} successfully deleted'}