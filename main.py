from lib2to3.pytree import Base
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Posts(BaseModel):
    title: str
    content: str

class Student(BaseModel):
    

@app.get("/")
async def get_user():
    return{"message:":"Hello World !"}

@app.get("/posts")
async def get_posts():
    return{"data:":"Welcome to the API world !"}

@app.post("/createPosts")
async def createPosts(payLoad: dict = Body(...)):
    print(payLoad)
    #return{"PayLoad":"successfully created the post"}
    return{"new_post:": f"title: {payLoad['title']} content: {payLoad['content']}"}