from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class Item(BaseModel):
    title: str
    description: str
    completed: bool = False
   
item_db = []

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item_db.append(item)
    return item  

@app.get("/items/", response_model=List[Item])
def read_item():
    return item_db

if __name__ == "__main__":
    uvicorn.run("Variant_5_8:app", host="127.0.0.1", port=5001,  reload=True)