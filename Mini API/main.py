from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import uuid

app = FastAPI()

# Pydantic Models are like descriptions of how a message should look
# This can work forwards and backwards! You can detail how responses should look
class CreateUser(BaseModel):    
    user_name: str                   # Models are like doorways, defning a shape data must follow to pass. 
    email: str                       # They defgine what the client may send, what we store, and what we send back.
    age: int                         # For example: CreateUser is a model that defines what is send for user creation.

class User(CreateUser):              
    user_id: uuid.UUID      
    
# Does not return email or age since it is not needed
class UserResponse(BaseModel):
    user_id: uuid.UUID
    user_name: str
    
    
users = []


@app.get("/")
def say_hi():
    return Response("Hi There")

# Create a user
@app.post("/users", status_code=201, response_model=UserResponse) # When the client calls post it will send a user, Status Code returned for resource created
def create_user(user: CreateUser):
    user_id = uuid.uuid4()           # Generate a user id
    new_user = User(**user.model_dump(), user_id=user_id) # Unpacking works on Python dictionaries but not Pydantic Models 
    users.append(new_user) 
    return new_user                  # FastAPi automatically converts to JSON

# Get all users
@app.get("/users", response_model=list[UserResponse]) # Responds with an array of UserResponse Objects          
def get_users():
    return {'users': users}  

# Get a specific user 
@app.get("/users/{user_id}", response_model=UserResponse)         
def get_specific(user_id: uuid.UUID):
    for user in users:
        if user.user_id == user_id: return user
    raise HTTPException(404, "User Not Found")

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: uuid.UUID, user: CreateUser):
    for i, stored_user in enumerate(users):
        if stored_user.user_id == user_id: 
            users[i] = User(**user.model_dump(), user_id=user_id)
            return Response(status_code=200)
    raise HTTPException(404, "User Not Found")
    
@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: uuid.UUID):
    for user in users:
        if  user.user_id == user_id: 
            users.remove(user)
            return Response(status_code=204)
    raise HTTPException(404, "User Not Found")
