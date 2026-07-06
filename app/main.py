from fastapi import FastAPI
from .routes import upload, jobs
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def root():
    return {"message": "Hello this is media processing API"}


app.include_router(upload.router)
app.include_router(jobs.router)

Instrumentator().instrument(app).expose(app)
