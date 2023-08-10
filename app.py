from fastapi import FastAPI
from src import users
from src import images
from utils.minio import connect_minio
from db.connection import create_database
from config.settings import create_settings

app = FastAPI(debug=True, on_startup=[create_settings, create_database, connect_minio])
app.include_router(users.router, prefix="/user")
app.include_router(images.router, prefix="/image")