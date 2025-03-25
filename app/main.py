from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API de monitoramento climático online"}