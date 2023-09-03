from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Baa"} , {"item_name" : "Baz"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("items2/{item_id}")
async def read_items2(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item