from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()


class CreateUser(BaseModel):    
    user_name: str                   # Models are like doorways, defning a shape data must follow to pass. 
    email: str                       # They defgine what the client may send, what we store, and what we send back.
    age: int                         # For example: UserCreate is a model that defines what is send for user creation.

class User(CreateUser):              
    user_id: uuid.UUID                                   
    
users = []

# Create a user
@app.post("/users")                  # When the client calls post it will send a user
def create_user(user: CreateUser):   # User object parameter
    user_id = uuid.uuid4()           # Generate a user id
    new_user = user.model_dump()     # Turn into a python dictionary 
    new_user["user_id"] = user_id    
    users.append(new_user) 
    return new_user                  # FastAPi automatically converts to JSON

# Get all users
@app.get("/users")                   
def get_users():
    return {'users': users}  

# Get a specific user 
@app.get("/users/{user_id}")         
def get_specific(user_id: uuid.UUID):
    for user in users:
        if user["user_id"] == user_id: return user
    return {"status": "not found"}

@app.put("/users/")
def update_user(user):
    for server_user in users:
        if server_user["user_id"] == user.user_id # Update some feature?
    return {"status": "success"}
    
@app.delete("/users/{user_id}")
def delete_user(user_id):
    for user in users:
        if user["user_id"] == user_id: users.remove(user)
    return {"status": "success"}

