import os

from fastapi import FastAPI

from lib.db_interface import DBInterface

app = FastAPI()

db_addr = os.environ.get("PROMETHEUS_ADDR", "http://127.0.0.1:9090/")
db = DBInterface(addr=db_addr)


@app.get("/")
def read_root():
    return [
        "/overview/",
        "/components/",
        "/components/{name}/",
    ]


@app.get("/overview/")
def get_overview():
    overview = db.get_overview()
    return overview


@app.get("/components/")
def get_components_or_details(name: str | None = None, view: str = "quarter"):
    if not name:
        components = db.list_components()
        return components

    component = db.get_component(name=name, view=view)
    return component
