import time
from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime

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

class Movie(BaseModel):
    id: int
    title: str
    author: str
    year: int
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str
    author: str = Field(min_length=3, max_length=30)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    category: str = Field(min_length=3, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                'id': 1,
                'title': 'my title',
                'author': 'John',
                'year': 2020,
                'category': 'action'
            }
        }
    }

    ## custom validations
    @validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('Title field muts have a minimun lenght of 5 caharacters')
        if len(value) > 20:
            raise ValueError('Title field muts have a maximun lenght of 15 caharacters')
        return value

class MovieUpdate(BaseModel):
    title: str
    author: str
    year: int
    category: str


app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

movies: list[Movie] = []


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

@app.get('/allMovies', tags=['Movies'], status_code=200, response_description="successfull request (John)")
async def get_all_movies() -> List[Movie]: # returning a List of movies
    # time.sleep(100)
    return JSONResponse(content=movies, status_code=200)

# to send a parameter do this:
@app.get('/movies/{id}', tags=['Movies'])
async def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie["id"] == id:
            return JSONResponse(content=movie)
    return JSONResponse(content={}, status_code=404)

#Query parameters
#parameters added only in the function
@app.get('/movies/', tags=['Movies'])
async def get_movie_by_category(_category: str = Query(min_length=5, max_length=20)) -> Movie | dict: ## retornando tipo
    for movie in movies:
        if movie['category'] == _category:
            return JSONResponse(content=movie, status_code=200)
    return JSONResponse(content={}, status_code=404)

##### POST ############
## Request body
@app.post('/movies', tags=['Movies'])
async def create_movie(movie: MovieCreate):

    movies.append(movie.model_dump())

    return "Ok"

@app.put("/movies/{id}", tags=['Movies'])
async def update_movie(id: int, _movie: MovieUpdate):
    
    for item in movies:
        if item["id"] == id:
            item["title"] = _movie.title
            item["year"] = _movie.year
            item["category"] = _movie.category
            item["author"] = _movie.author

    return movies

@app.delete("/movies/{id}",  tags=['Movies'])
async def delete_movie(id: int):
    for movie in movies:
        if(movie["id"] == id):
            movies.remove(movie)

    return [movie.model_dump() for movie in movies]


