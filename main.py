from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
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
    title: str = Field(min_length=3, max_length=15) # data validation
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
    return "Hola preciosa"

@app.get('/dictionary', tags=['Home'])
def home():
    return {"name": "test"}

@app.get('/html', tags=['Home'])
def home():
    return HTMLResponse('<h1> html element</h1>')

@app.get('/allMovies', tags=['Movies'])
def get_all_movies() -> List[Movie]: # returning a List of movies
    return movies

# to send a parameter do this:
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(_id: int) -> Movie:
    for movie in movies:
        if movie['id'] == _id:
            return movie
    return []

#Query parameters
#parameters added only in the function
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(_category: str, _year: int) -> Movie: ## retornando tipo
    for movie in movies:
        if movie['category'] == _category:
            return movie.model_dump()
    return []

##### POST ############
## Request body
@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate):

    movies.append(movie.model_dump())

    return "Ok"

@app.put("/movies/{id}", tags=['Movies'])
def update_movie(id: int, _movie: MovieUpdate):
    
    for item in movies:
        if item["id"] == id:
            item["title"] = _movie.title
            item["year"] = _movie.year
            item["category"] = _movie.category
            item["author"] = _movie.author

    return movies

@app.delete("/movies/{id}",  tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if(movie["id"] == id):
            movies.remove(movie)

    return [movie.model_dump() for movie in movies]


