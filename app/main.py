from fastapi import FastAPI
from .models import init_db
from .routers import orders

app = FastAPI(title="Trade Orders API", version="1.0.0")
app.include_router(orders.router, prefix="/orders")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"message": "Welcome to the Trade Orders API!"}
