NOTES:

* run the application: uvicorn main:app
    -main: is the filename (main.py)
    -app: application name
    -5000: is the port
* habia nombrado mi archivo como api pero parece que es una palabra reservada NO USARLO
 
* to change the port use this command: uvicorn main:app --port 5000
 where:
    -main: is the filename (main.py)
    -app: application name
    -5000: is the port

* to reload automatically add this parameter: --reload
* to access to the app from other devices add this parameter: --host 0.0.0.0
  IMPORTANT: all devices are in the same network can access to the app

* to see the documentation add baseURL + /docs for example: http://127.0.0.1:8000/docs

* another page to see documentation use this route: http://127.0.0.1:8000/redoc



to allow run scripts in windows (run in power shell): Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass