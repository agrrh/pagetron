import os

import ttl_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from lib.db_interface import DBInterface

DEFAULT_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

# Pings are not more frequent that 15s
CACHE_TTL_DEFAULT = 15.0 * 1.5

app = FastAPI()

origins = [
    _ for _ in os.environ.get("APP_CORS_ORIGINS", "").split(",") if _
] or DEFAULT_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

db_addr = os.environ.get("PROMETHEUS_ADDR", "http://127.0.0.1:9090/")
db = DBInterface(addr=db_addr)


@app.get("/")
def read_root():
    return [
        "/overview/",
        "/components/",
        "/components/?name={name}",
    ]


@app.get("/overview/")
@ttl_cache(CACHE_TTL_DEFAULT)
def get_overview():
    overview = db.get_overview()
    return overview


@app.get("/components/")
@ttl_cache(CACHE_TTL_DEFAULT)
def get_components_or_details(name: str | None = None, view: str = "quarter"):
    if not name:
        components = db.list_components()
        return components

    component = db.get_component(name=name, view=view)
    return component


# @app.get("/full/")
# @ttl_cache(CACHE_TTL_DEFAULT)
# def get_full():
#     views = ("quarter", "hours", "year")
#
#     data = {}
#
#     data["overview"] = db.get_overview()
#     data["components"] = db.list_components()
#
#     data["data"] = {}
#
#     for component in data["components"]:
#         data["data"][component] = {}
#
#     for component in data["components"]:
#         for view in views:
#             data["data"][component][view] = db.get_component(name=component, view=view)
#
#     return data
