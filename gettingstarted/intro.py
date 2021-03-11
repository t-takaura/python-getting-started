from fastapi import FastAPI

app = FastAPI()

@app.get("/") # methodとendpontの指定
async def hello():
    return {"text": "hello world!"}
