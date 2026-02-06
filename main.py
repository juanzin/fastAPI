from fastapi import Depends, FastAPI, Header, Request, Response, HTTPException
from typing import Annotated

app =  FastAPI()
app.title = "FAST API TEST"
app.version = "2.0.0"

# header parameters help us to send extra information to the server, I didn't understand it

## version 1
'''
@app.get('/dashboard')
def dashboard(
    request: Request,
    response: Response,
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[str | None, Header()] = None
    ):
    print(request.headers)
    response.headers["user_status"] = "enabled"
    return {"access_token": access_token, "user_role": user_role}

'''

## version 2
def get_headers(
    access_token: Annotated[str | None, Header()] = None,
    user_role: Annotated[str | None, Header()] = None
):
    if access_token != "secret-token":
        raise HTTPException(status_code=401, detail="No authorized")
    return {"access_token": access_token, "user_role": user_role}

@app.get('/dashboard')
def dashboard(headers: Annotated[dict, Depends(get_headers)]):
   
    return {"access_token": headers["access_token"], "user_role": headers["user_role"]}

