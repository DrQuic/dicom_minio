from fastapi import APIRouter, Depends, Request, UploadFile
from dto.user import User, UserMultipart
from utils.minio import get_client, MinioUtil

router = APIRouter()

async def parse_request(request: Request):
    form = await request.form()
    user = User(name=form.get("name"), last_name=form.get("last_name"), age=form.get("age"))
    profile_picture = form.get("profile_picture")
    return user, profile_picture

@router.post("/")
async def store_user(data:(User, UploadFile) = Depends(parse_request), minio: MinioUtil = Depends(get_client)):
    user, profile_picture = data
    result_file= minio.store_png(profile_picture)
    print(result_file.object_name)
    return {"result_name": result_file.object_name} 