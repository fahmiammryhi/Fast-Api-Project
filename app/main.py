from fastapi import FastAPI
from .routers import account
from config import FLIP_SECRET

app = FastAPI()

app.include_router(account.router)

@app.get("/")
def root():
    return {"flip_secret": FLIP_SECRET}
