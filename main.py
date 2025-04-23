from fastapi import FastAPI

app = FastAPI()

app.get("/")
async def hello_word():
    return "Hello World"