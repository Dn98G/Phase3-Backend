#import the fastapi package here
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import UsersSchema, NotesSchema, TagsSchema, status
from models import Users, Notes, Tags, get_db
from sqlalchemy.orm import Session

#this initializes it

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])



@app.get('/users')
def get_all_users(user_id: int, session: Session = Depends(get_db)):
    
    user = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user

@app.post('/Users/{user_id}')
def add_user(user: UsersSchema, session: Session = Depends(get_db)):
    
    new_user = Users(**user.model_dump())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {'message':'User {new_notes.id} has been successfully added!'}

@app.patch('/users/{user_id}')
def update_user(user_id: int, user: UsersSchema, session: Session = Depends(get_db)):

    doctor = session.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Userr with id {user_id} not found"
        )

@app.delete('/users/{user_id}')
def delete_user(user_id:int, session: Session = Depends(get_db)):
    
    user = session.query(Users).filter(Users.id == user_id).first()
    session.delete(Users)
    
    session.commit()
    return {'message':'user {user_id} successfully deleted'}


@app.get('/Notes')
def get_all_notes(notes_id: int, session: Session = Depends(get_db)):
    
    doctor = session.query(Notes).filter(Notes.id == Notes.id).first()
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notes with id {notes_id} not found"
        )
    return Notes

@app.post('/Notes/{notes_id}')
def add_notes(notes: NotesSchema, session: Session = Depends(get_db)):
    
    new_notes = Notes(**notes.model_dump())
    session.add(new_notes)
    session.commit()
    session.refresh(new_notes)
    return {'message':'notes {new_notes.id} has been successfully added!'}

@app.patch('/notes/{notes_id}')
def update_notes(user_id: int, notes: NotesSchema, session: Session = Depends(get_db)):

    notes = session.query(Notes).filter(Notes.id == Notes.id).first()
    if not notes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Notes with id {Notes.id} not found"
        )

@app.delete('/notes/{notes_id}')
def delete_notes(notes_id:int, session: Session = Depends(get_db)):
    
    notes = session.query(Notes).filter(notes.id == notes_id).first()
    session.delete(Notes)
    
    session.commit()
    return {'message':'notes {notes_id} successfully deleted'}

@app.get('/Tags')
def get_all_tags(tag_id: int, session: Session = Depends(get_db)):
    
    tag = session.query(Tags).filter(Tags.id == Tags.id).first()
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {tag_id} not found"
        )
    return tag

@app.post('/Tags/{tag_id}')
def add_tag(tag: TagsSchema, session: Session = Depends(get_db)):
    
    new_tag = Tags(**tag.model_dump())
    session.add(new_tag)
    session.commit()
    session.refresh(new_tag)
    return {'message':'tag {new_tag.id} has been successfully added!'}

@app.patch('/tagss/{user_id}')
def update_tag(tag_id: int, tag: TagsSchema, session: Session = Depends(get_db)):

    Tag = session.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tag with id {tag_id} not found"
        )

@app.delete('/tags/{tag_id}')
def delete_tag(tag_id:int, session: Session = Depends(get_db)):
    
    tag = session.query(tag).filter(tag.id == tag_id).first()
    session.delete(tag)
    
    session.commit()
    return {'message':'tag {tag_id} successfully deleted'}
