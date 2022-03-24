from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="TODO List | By Prince",v1=1.0)

class Todo(BaseModel):
    name:str
    due_date:str
@app.get("/")
async def hello():
    return {"hello":"world"}
