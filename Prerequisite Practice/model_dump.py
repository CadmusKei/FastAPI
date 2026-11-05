from pydantic import BaseModel

class User(BaseModel):
    username: str # Anything without a default value, is required!
    age: int = 18
    fav_colour: str = "blue"

# This runs, but if the types to not match the pydantic models it will crash! 
user = User(
    username="Cadmus",
    age=21
)

# Converts BaseModel data to python Dictionary
print(user.model_dump())