from fastapi import FastAPI
from controlers import rota
from database import sync_database,get_engine

main = FastAPI()

sync_database(get_engine())

main.include_router(router=rota,prefix="/api/geek")