import time
from fastapi import FastAPI, Body, Path, Query, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import datetime
from src.models.movie_model import Movie, MovieCreate, MovieUpdate

movies: list[Movie] = []
movie_router = APIRouter()

@movie_router.get('/getAllMovies', tags=['Movies'], status_code=200, response_description="successfull request (John)")
async def get_all_movies() -> List[Movie]: # returning a List of movies
    return JSONResponse(content=movies, status_code=200)

# to send a parameter do this:
@movie_router.get('/by-id/{id}', tags=['Movies'])
async def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie["id"] == id:
            return JSONResponse(content=movie)
    return JSONResponse(content={}, status_code=404)

#Query parameters
#parameters added only in the function
@movie_router.get('/by_category', tags=['Movies'])
async def get_movie_by_category(category: str = Query(min_length=3, max_length=20)) -> Movie | dict: ## retornando tipo
    for movie in movies:
        if movie['category'] == category:
            return JSONResponse(content=movie, status_code=200)
    return JSONResponse(content={}, status_code=404)

##### POST ############
## Request body
@movie_router.post('/', tags=['Movies'])
async def create_movie(movie: MovieCreate):

    movies.append(movie.model_dump())

    return "Ok"

@movie_router.put("/{id}", tags=['Movies'])
async def update_movie(id: int, _movie: MovieUpdate):
    
    for item in movies:
        if item["id"] == id:
            item["title"] = _movie.title
            item["year"] = _movie.year
            item["category"] = _movie.category
            item["author"] = _movie.author

    return movies

@movie_router.delete("/{id}",  tags=['Movies'])
async def delete_movie(id: int):
    for movie in movies:
        if(movie["id"] == id):
            movies.remove(movie)

    return movies