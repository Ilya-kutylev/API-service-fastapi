import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .utils import find_path, load_structure

app = FastAPI()


class ElementPath(BaseModel):
    element_id: str


@app.post("/get_path/")
async def get_path(data: ElementPath):
    structure = await load_structure()
    path = await find_path(structure, data.element_id)
    if path is None:
        raise HTTPException(status_code=404, detail="ID element is not found in structure")
    return path


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)