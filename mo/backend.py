from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory= BASE_DIR)


@app.get("/", response_class=HTMLResponse)
def learn(request: Request):
    return templates.TemplateResponse("index-mod.html",{"request": request})

@app.post("/login",response_class= HTMLResponse)
def learn_login(request: Request, username:str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse("success.html", {"request": request})