from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items12/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item-id": item_id}
    if q:
        results.update({"q": q})
    return results

'''
ge : greater than or equal, 크거나 같다
gt : greater than, 크다
lt : less than, 작다
le : less than or equal, 작거나 같다
'''
@app.get("/items13/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The Id of the item to get",ge=1),q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results
'''
def func(a=10,b):    => 에러
def func(a,b=10)     => OK
즉 default value를 뒤에 두는게 좋다
'''
@app.get("/items14/{item_id}")
async def read_items(
    q: str, item_id: int = Path(..., title="The Id of the item to get",ge=1)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results
