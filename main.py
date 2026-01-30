from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

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

@app.get('/movies', tags=['Home'])
def home():
    return [
        {
            "title": "movie 1",
            "author": "john",
            "category": "romantic"
        },
        {
            "title": "my love",
            "author": "John",
            "category": "romantic"
        }
    ]