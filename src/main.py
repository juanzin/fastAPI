import time
from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse, Response
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request

## model
# para definir una propiedad como opcional podemos hacerlo de la siguiente manera: int | None = None
# o usando typing: Optional[int]

# data validation
# Field(min_length=5, max_length=15)
# gt greather than
# ge greather than or equal
# lt less than
# le less than or equal

# you can add default values using the parameter <<default>> example: Field(min_length=5, max_length=15, default="no title")
# or you can use: model_config... see the example in movieCreate
# the next funcion converts to dictionary: movie.model_dump()

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

##### middleware section
# app.add_middleware(HTTPErrorHandler) # this using HTTPErrorHandler (http_error_handler.py)
@app.middleware('http') # this middlware was added using  FAST API
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    print("middleware is running...")
    # call_next is executed before my endpoint, this is:
    # client -> middleware -> myEndpoint
    return await call_next(request)

##### end middleware section

@app.get('/')
def home():
    return "Hola bonita"

@app.get('/', tags=['Home'])
def home():
    return PlainTextResponse(content="Hola preciosa")

@app.get('/redirect', tags=['Home'])
def redirect():
    return RedirectResponse("/allMovies", status_code=303)

@app.get('/getFile', tags=['Home'])
def getFile():
    return FileResponse("book.pdf")

@app.get('/dictionary', tags=['Home'])
def home():
    return {"name": "test"}

@app.get('/html', tags=['Home'])
def home():
    return HTMLResponse('<h1> html element</h1>')

app.include_router(prefix="/movies", router=movie_router)