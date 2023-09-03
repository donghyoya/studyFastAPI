from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name" : "Foo"}, {"item_name" : "Baa"} , {"item_name" : "Baz"}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db