import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse, Response
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.requests import Request
## templates
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
# dependecies
from fastapi import Depends, Query
from typing import Annotated

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

## GLOBAL DEPENDENCIES
def denpendency1():
    # you can add parameters in the function, but they will required in all endpoints
    # because is a global dependency
    print("dependency 1")

def denpendency2():
    print("dependency 2")

## END GLOBAL DEPENDENCIES

app =  FastAPI(dependencies=[Depends(denpendency1), Depends(denpendency2)]) ## global dependency
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

## region templates
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

app.mount('/static', StaticFiles(directory=static_path), 'static')
templates = Jinja2Templates(directory=templates_path)
## end region templates

# @app.get('/')
# def home():
#     return "Hola bonita"

@app.get('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'message': 'Welcome'})

# dependecies
# WITH A FUNCTION
# def common_params(start_date: str, end_date: str):
#     return {"start_date": start_date, "end_date": end_date}

# commonDep = Annotated[dict, Depends(common_params)] # dependency with annotated, type = dict, dependency=common_params, this variable can be reused in customers


# WITH A CLASS
# use commons: commonDep = Depends(), where commonDep is the type
class commonDep:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

@app.get('/users', tags=['Users'])
def get_users(commons: commonDep = Depends()):
    return f"Users created between {commons.start_date} and {commons.end_date}"

@app.get('/customers', tags=['Users'])
def get_customers(commons: commonDep = Depends()):
    return f"Customers created between {commons.start_date} and {commons.end_date}"

# end depencies

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