from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI(title="TODO List | By Prince",v1=1.0)

class Todo(BaseModel):
    id:int
    name:str
    due_date:str
List_todo=[]
@app.get("/")
async def hello():
    return {"hello":"world"}

@app.post("/todo",response_model=Todo)
async def create_todo(todo:Todo):
    try:
        List_todo.append(todo.dict())
        return todo
    except:
        raise HTTPException(status_code=400,detail="Base de données inacessible")

@app.get('/todos',response_model=List[Todo])
async def get_all():
    return List_todo


@app.put("/todo",response_model=Todo)
async def update(id:int,new:Todo):
    try:
        List_todo[id]=new
        return new
    except:
        HTTPException(status_code=400,detail="Pas enregistré dans DB")
