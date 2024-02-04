from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/")
def read_root():
    return "Api de adopta la plata huila"

app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)