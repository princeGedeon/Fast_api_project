from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Coord(BaseModel):
    x:float
    y:float
    zoom:Optional[int]

@app.post("/position")
async def make_position(Coord:Coord):
    return {"new":Coord}

@app.get("/")
async def hello():
    return {"hello":"world"}

@app.get("/produit/{product_id}")
async def read_product(product_id:int,nom:Optional[str]=None):
    return {"id":product_id,"nom":nom}