
from pydantic import BaseModel

## Questions for Chat

# What is uvicorn
# What is a server process

# This is a pydantic model, it is a class that inherents BaseModel
class User(BaseModel):
    username: str # Anything without a default value, is required!
    age: int = 18
    fav_colour: str = "blue"

# This runs, but if the types to not match the pydantic models it will crash! 
user = User(
    username="Cadmus",
    age=21
)
print(user.fav_colour)

