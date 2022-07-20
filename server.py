# from urllib.request import Request
from fastapi import FastAPI
from model import Query
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime

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


# @app.get("/bot/{question}")
# async def chatbot(question: str):

#     answer = bot.Bot(question)
#     print(answer)
#     return {"Name": "JARVIS Inc.", "bot_response": answer}


# @app.post("/test")
# async def test(request : Request):
#     data = await request.json()
#     if(data["asd"]):
#         print("asd")
#     return await request.json()


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
    answer = bot.Bot(question)
    now = datetime.now
    data = {"bot": "Jarvis Inc.", "answer": answer, "time": now()}

    return data


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")
