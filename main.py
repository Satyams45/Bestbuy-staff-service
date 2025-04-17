from fastapi import FastAPI
from routes import router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Best Buy Staff Service",
    description="A microservice to manage staff info",
    version="1.0.0"
)

# Root path to avoid 404 error
@app.get("/")
def read_root():
    return {"message": "Welcome to Best Buy Staff Service"}

# Include staff-related routes
app.include_router(router)
