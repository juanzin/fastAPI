from fastapi import FastAPI

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

@app.get('/dashboard')
def home():
    return "dashboard"

