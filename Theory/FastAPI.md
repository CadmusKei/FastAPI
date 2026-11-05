# **FastAPI**

---

## **Pydantic and Validation**

Python is dynamically typed, but JSON and general backend processes require specified types for validation. A tool called `pydantic` is used to validate python data for backend processes. We use python's type hints

### Type Hints

```python
test: int = 4
age: int | None = "fooled!"

# They are not enforced, just hints
print(type(age))

```

### BaseModel

WIth these, we can create BaseModel models (classes) that can easily be passed as JSON. It requires type hints, and treats anything without a default value as required. 

```python
from pydantic import BaseModel

# This is a pydantic model, it is a class that inherents BaseModel
class User(BaseModel):
    username: str # Anything without a default value, is required!
    age: int = 18
    fav_colour: str = "blue"

# This runs, but if the types to not match the pydantic models it raises
# `ValidationError`! 
user = User(
    username="Cadmus",
    age=21
)
# Access value in class fasion rather than dicitonary
print(user.fav_colour)
```

### Model_Dump()

BaseModels can be converted back to python dictionaries with a some method called `model_dump()`. 

```python
from pydantic import BaseModel
class User(BaseModel):
    username: str 
    age: int = 18
    fav_colour: str = "blue"
user = User(
    username="Cadmus",
    age=21
)

# Converts BaseModel data to python Dictionary
print(user.model_dump())

# You can also return json
print(user.model_dump_json())
```

---

## **Decorators**

FastAPI uses decorators for Routing and CRUD. It is worth knowing a little about what they are or how they work. 

Imagine you have 50 functions, and you want to add something to those functions, or debug by printing in those functions, you would have to edit all those function, or make 50 new functions! It would be ideal if we could simply attach a line that indicates that function should do that extra stuff. Enter: decorators.

### Example without decorators

```python
def greet(name):
    return f"hello {name}"

def shouty_greet(name):          
    result = greet(name)         
    return result.upper()       
```

Now see if we add the decorator (the @), infront of a function. 

### Example with decorators

```python
# My wrapper function
def shout(func):
    def wrapper(text: str):
        result = func(text).upper()
        return result
    return wrapper

@shout
def new_greet(name):
    return ("Hello " + name)

@shout
def farewell(name):
    return ("goodbye " + name)

print(new_greet("Kei"))   # prints HELLO KEI
print(farewell("Max"))    # prints GOODBYE MAX
```

---

## **Basic routing and HTTP requests**

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()

# Remember we use HTTP requests from the clients perspective
@app.get("/") # GET request and route
def home():
    return {"message": "Hello"} # returning a dict will automatically return JSON

@app.post("/login") # POST request to /login route
def login():
    return {"Login": "Cadmus"}
```

> Run your first mini server: `uvicorn main:app --reload`

---

## **Path Parameters and Path Queries**

### Path Parameters 

A path parameter is like a path variable. It allows us to generalise routes. for example `/friends/users/1`, `/friends/users/2`, `/friends/users/3`. 

Then the `user_id` of the friends is the variable. 

```python
from fastapi import FastAPI 
app = FastAPI()

@app.get("/friends/users/{user_id}")  # We put the path paramter in the route
def get_friends(user_id: int):        # The fnction pulls the parameter
    return {'user-id': user_id}       # The function can now use it
```

### Query Parameters

What if we want to retrieve an object (or several) based on a query? (Like a filter)
Then we could have something like 

```python
# String
/blogs?post=My%20First%20Post
# or Int
/sample?size=30
# or Bool
/students?stem=True
# Or even several
/students?stem=true&year=2
```

When we query, we leave the functions generalised for any kind of query: 

```python
from fastapi import FastAPI

app = FastAPI()

# String
@app.get("/blogs")
def get_blog(post: str):
    return {"post": post}

# Integer
@app.get("/sample")
def get_sample(size: int):
    return {"size": size}

# Boolean
@app.get("/students")
def get_students(stem: bool = False):
    return {"stem": stem}
```

---

