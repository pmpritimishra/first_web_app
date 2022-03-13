# create a FastAPI CODE
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()
class Employee(BaseModel):
    name:str
    age:int
    number: str
    experience: int 
    street:str
    organization:str
    description: Optional[str] = None
class STUDENT(BaseModel):
    name:str
    department:str
    id:int
    age:int
    phone:int

#end point test we pass some value inside get
#for get input from user using GET method
@app.get("/welcome/{my_query}")
def home(my_query,Q:Optional[str]=None):
     return {"message":"Welcome to digital World","user_input":my_query,"query":Q}
#above same code test with postman
@app.put("/endpoint")
async def endpoint(resume:Employee):
    return {"username":resume.name}
#post method
@app.post("/mypostendpoint")
async def mpep(stu:STUDENT):
    return {"stu":stu.name}

