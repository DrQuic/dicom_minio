from fastapi import FastAPI,Depends
from routes import dicoms
from routes import users
from utils.minio import connect_minio
app = FastAPI(debug=True, dependencies=[Depends(connect_minio)])
app.include_router(dicoms.router, prefix="/dicom")
app.include_router(users.router, prefix="/user")