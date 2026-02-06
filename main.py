import time
from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"


@app.get('/hello')
def home():
    return "Hola bonita"


