# from urllib.request import Request
from fastapi import FastAPI
from model import Query
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware





import bot

app = FastAPI()


@app.get("/")
async def root():
    data = {
        "Name": "JARVIS",
        "Validations": "You should add your question to query paramaters",
        "Route for chatbot": "/bot/your_question",
        "Built": "Its was built for DBMS project",
        "Inventor": "I was Created by CIS Students batch 2020 (20105, 20052, 20301, 20107)",
        "Language": "Pure English ",
    }

    return data


@app.get("/bot/")
async def chatbot():
    data = {
        "Bot Request": "It should be send as question in body request",
        "Backend": "It may take some while ml model runing in background Using -Fast Api",
    }
    return data


@app.post("/bot/")
async def create_query(query: Query):
    question = query.question
    try: 
        answer = bot.Bot(question)
    except Exception as e :
        return {"error": "Something Went wrong the server or bot", "exception": e}
    
    now = datetime.now
    data = {"bot": "Jarvis Inc.", "answer": answer, "time": now()}

    return data


# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     return RedirectResponse("/")


# config 
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)