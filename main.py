from fastapi import FastAPI, Form, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi.exceptions import HTTPException
from jose import jwt

## authentication and autorization
# using auth2
# it is required: pip install python-multipart
# it is required: pip install python-jose


app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") ## tokenurl is an endpoint, see #1

users = {
    "Juan": {
        "username": "Juan",
        "email": "juan_1020@hotmail.com",
        "password": "fakepass"
    },
    "Gabriela": {
        "username": "Gaby",
        "email": "Gabs@gmail.com",
        "password": "pretty123"
    }
}
secret_code = "Kiss me"  # secret code should be saved in a secure place, research about this
algorithm = "HS256" # Research about algoritms
def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, secret_code, algorithm=algorithm) # create token with user data
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, secret_code, algorithms=[algorithm]) # get user data using token
    user = users.get(data["username"])
    return user

@app.post('/token') # this is the tokenUrl #1
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)

    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=400, detail="User does not exist or password is incorrect")
    
    token = encode_token({"username": user["username"], "email": user["email"]})
    return {"access_token": token}

@app.get("/users/profile")
def profile(my_user: Annotated[dict, Depends(decode_token)]): # with Annotated[dict, Depends(decode_token)] we are protecting the endpoint
    return my_user