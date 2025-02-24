from fastapi import FastAPI
from .models import init_db
from .routers import orders

def create_app():
    app = FastAPI(title="Trade Orders API", version="1.0.0")
    app.include_router(orders.router)
    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    # Initialize DB tables
    init_db()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Trade Orders API!"}
