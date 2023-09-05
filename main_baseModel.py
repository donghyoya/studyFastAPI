from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/item/")
async def create_item(item: Item):
    return item

@app.post("/items/")
async def create_item(item: Item):
    # item.dict() == item.model_dump()
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
'''
입력할때 http://127.0.0.1/items/{items_id}?item=id 하고 
reqeust body 작성하고 호출해야한다
'''
@app.put("/items/{items_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q":q})
    return result