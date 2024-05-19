from fastapi import FastAPI
from starlette.requests import Request

from bochka.orm.database import Database

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.middleware("http")
async def db_session_middleware(request: Request, call_next, db: Database = Database()):
    request.state.db = db.get_session()
    response = await call_next(request)
    request.state.db.close()
    return response
