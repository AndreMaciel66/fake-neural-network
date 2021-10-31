from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from app.fake_kpi_tree_generator import Tree
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Fake": "Data"}


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
