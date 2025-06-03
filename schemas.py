from pydantic import BaseModel

class UsersSchema(BaseModel):
    name:str
    age:int
    phone_number:int
    address:str
    account_types:str

class NotesSchema(BaseModel):
    code : int
    details: str
    content:str
    id:int
    title:str
    
class TagsSchema(BaseModel):
    code : int
    details: str
    name:str
    id:int
    title:str   