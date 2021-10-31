from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from app.fake_kpi_tree_generator import Tree
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

class Paths(BaseModel):
    name: str
    parents: list
    childs: list


@app.get("/tree")
def read_tree(response_model=List[Paths]):
    tree = Tree(5, 5)
    tree.generate_metric_rows()
    tree.generate_random_metrics()
    tree.randomize_network()
    print(tree.all_paths)
    return tree.all_paths


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
