from fastapi import APIRouter, UploadFile, Depends
from config.settings import Settings, get_settings
from utils.minio import MinioUtil, get_client
router = APIRouter()


@router.post("/")
async def store_dicom(file: UploadFile, minio: MinioUtil = Depends(get_client)):
    #content = await file.read(132)
    file_content = await file.read(130) 
    #print(content.decode()[-4:] == "DICM")
    print( "DICM" in str(file_content))
    return {"status": "ok"}

