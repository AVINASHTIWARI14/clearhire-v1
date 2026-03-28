from fastapi import FastAPI
from routers import analyze

app = FastAPI()

app.include_router(analyze.router)

@app.get("/")
def home():
    return {"message": "clearhire backend is running"}