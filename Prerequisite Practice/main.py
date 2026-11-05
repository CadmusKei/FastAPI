from fastapi import FastAPI

app = FastAPI()

# NB We use HTTP requests from the clients persepective
@app.get("/")
def home():
    return {"message": "Hello"}

@app.get("/login")
def logn():
    return {"Login": "Cadmus"}