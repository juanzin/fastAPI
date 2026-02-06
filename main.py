from fastapi import FastAPI, Response, Cookie
from fastapi.responses import JSONResponse


# COOKIES
# a cookie allows data to be stored in the browser like user data or navigation data
# you can create cookies from client using JS or you can create them in the server
# which is the best way to create cookies?

# structures cookie:
# username: John; expires: Thu, 18...; path=/
# expires=10 # cookie will expire in 10 seconds
# path="/users" cookie is only available for the path /users, it is not available in dashboard or another endpint diferent to /users

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

@app.get('/') # create cookie: version 1
def root(response: Response):
    response.set_cookie(key="username", value="Juan")
    return JSONResponse(content={"msg": "welcome"}, headers={"set-cookie": "username=Juan"})

@app.get('/users') # create cookie: version 2
def root(response: Response):
    response = JSONResponse(content={"msg": "welcome"})
    response.set_cookie(key="username", value="Juan", expires=10, path="/users")
    return response

@app.get('/dashboard') # get cookie
def dashboard(username: str = Cookie()):
    return username
    
