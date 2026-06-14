from fastapi import FastAPI
from .routes import upload
app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello this is media processing API"}

app.include_router(upload.router)
