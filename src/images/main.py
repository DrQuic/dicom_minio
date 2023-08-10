from fastapi import APIRouter, Depends
from utils.minio import get_client, MinioUtil

router = APIRouter()

@router.get("/{bucket}/{id}")
async def get_image(
    bucket: str,
    id: str,
    minio: MinioUtil = Depends(get_client),
):
    return minio.client.get_object(bucket_name=bucket, object_name=id)