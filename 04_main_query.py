from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items3/")
async def read_items(q: Optional[str] = None):
    result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        result.update({"q":q})
    return result

@app.get("/items4/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
^ : 뒤에나오는 문자로 시작한다. 즉 q값은 무조건 fixedquery로 시작함
$ : 정규식의 끝마침. 이 뒤로 문자가 올 수 없다
'''
@app.get("/items5/")
async def read_items(q: Optional[str] = Query(None, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
아래는 아무값이 안들어가면 리턴값이
defaultquery 로 나온다
'''
@app.get("/items6/")
async def read_items(q: str = Query("defaultquery", max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
'''
아래는 굳이 값을 않넣어도 되게끔 한데
'''
@app.get("/items7/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items8/")
#q: List[str] = q: list
async def read_items(q: list = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items
'''
title, description 으로 metadata로 추가할수있다
즉 설명을 작성한다?
'''
@app.get("/items9/")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        )
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results
'''
item-query를 param 변수명으로 지정할수 없지만
아래처럼 설정하면 변수명으로 사용이 가능하게끔 한다
'''
@app.get("/items10")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results
'''
만약 어떤 파라미터를 업데이트하거나 관리하기 싫다고 하자
하지만 그 파리미터를 삭제하면 안된다. 그걸 쓰는 유저들이 있을테니
그럴때 deprecated를 표시해주면 된다
아래처럼 Query를 선언 해 줄 때 deprecated=True를 해주자
'''
@app.get("/items11/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        
        deprecated=True,

    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results