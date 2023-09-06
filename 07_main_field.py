from typing import Optional, Set, List
from fastapi import Body, FastAPI

from pydantic import BaseModel, Field


app = FastAPI()

class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

class Item2(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

    images: Optional[Image] = None

class Item3(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

    images: Optional[List[Image]] = None


@app.put("/items17/{item_id}")
async def update_item(item_id: int, item: Item = Body(...,embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

@app.put("/items18/{item_id}")
async def update_item(item_id: int, item: Item2 = Body(...
    ,example={
                {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2,
            "tags": ["rock", "metal", "bar"],
            "image": {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            }
        }
    }
)):
    result = {"item_id": item_id, "item":item}
    return result

@app.put("/items19/{item_id}")
async def update_item(item_id: int, item: Item3):
    result = {"item_id": item_id, "item":item}
    return result

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image] = Body(...
    ,example={
        [ 
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    },
)):
    return images