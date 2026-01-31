from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

## model
# para definir una propiedad como opcional podemos hacerlo de la siguiente manera: int | None = None
# o usando typing: Optional[int]

# data validation
# Field(min_length=5, max_length=15)

class Movie(BaseModel):
    id: int
    title: str
    author: str
    year: int
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15) # data validation
    author: str
    year: int
    category: str

class MovieUpdate(BaseModel):
    title: str
    author: str
    year: int
    category: str


app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

movies = [
        {
            "id": 1,
            "title": "movie 1",
            "author": "john",
            "year": 2000,
            "category": "action"
        },
        {
            "id": 2,
            "title": "my love",
            "author": "John",
            "year": 2020,
            "category": "romantic"
        }
]


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
            return movie
    return []

##### POST ############
## Request body
@app.post('/movies', tags=['Movies'])
def create_movie(movie: Movie):

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

    return movies


