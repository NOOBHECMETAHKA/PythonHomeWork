from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.responses import FileResponse


def information() -> dict:
    all_cats = dict()
    all_cats[1] = (Cat(name="Барсик", age=5))
    all_cats[2] = (Cat(name="Пуфик", age=6))
    all_cats[3] = (Cat(name="Гардион", age=8))
    return all_cats


app = FastAPI(debug=True)


class Cat(BaseModel):
    name: str
    age: Optional[int] = 0


MEMORY_DB = information()


@app.get("/")
def root():
    return FileResponse("index.html")


@app.get("/cats")
async def index():
    return {"data": MEMORY_DB}


@app.get("/cats/first")
async def first():
    return {"data": MEMORY_DB[min(MEMORY_DB.keys())]}


@app.get("/cats/lastest")
async def lastest():
    return {"data": MEMORY_DB[max(MEMORY_DB.keys())]}


@app.get("/cats/{id}")
async def show(id: int, response: Response):
    cat = MEMORY_DB.get(id)
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with id not exists!")
    return {"data": cat}

@app.post("/cats")
async def store(newCat:Cat):
    MEMORY_DB[len(MEMORY_DB) + 1] = newCat.model_dump()
    return {"data": "post created", "new cat": newCat}


if __name__ == '__main__':
    uvicorn.run(app, port=8081)
