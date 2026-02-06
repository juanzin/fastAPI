from fastapi import FastAPI
from sqlmodel import SQLModel
from app.config.database import engine
from app import models
from app.routes.item_router import items_router

# it requires: pip install sqlmodel pymysql
# to connect to mysql server

SQLModel.metadata.create_all(engine) # connect to the database

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

@app.get('/')
def home():
    return "Hola bonita"


app.include_router(items_router)

