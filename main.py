from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

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
def home():
    return movies

# to send a parameter do this:
@app.get('/movies/{id}', tags=['Movies'])
def get_movie(_id: int):
    for movie in movies:
        if movie['id'] == _id:
            return movie
    return []

#Query parameters
#parameters added only in the function
@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(_category: str, _year: int):
    for movie in movies:
        if movie['category'] == _category:
            return movie
    return []

##### POST ############
## Request body
@app.post('/movies', tags=['Movies'])
def create_movie(
    id: int = Body(), 
    year: int = Body(),
    category: str = Body(),
    title: str = Body(),
    author: str = Body()):

    movies.append({
        "id": id,
        "year": year,
        "category": category,
        "title": title,
        "author": author
    })

    return "Ok"

@app.put("/movies/{id}", tags=['Movies'])
def update_movie(
    id: int,
    year: int = Body(),
    category: str = Body(),
    title: str = Body(),
    author: str = Body()):
    
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["year"] = year
            movie["category"] = category
            movie["author"] = author

    return movies

@app.delete("/movies/{id}",  tags=['Movies'])
def delete_movie(id: int):
    for movie in movies:
        if(movie["id"] == id):
            movies.remove(movie)

    return movies