from minio import Minio
from fastapi import UploadFile
from config.settings import get_settings, Settings
from uuid import uuid4

class MinioUtil:
    def __init__(self):
        settings: Settings = get_settings()
        self.client = Minio(
            endpoint=settings.miniouri,
            access_key=settings.miniokey,
            secret_key=settings.miniosecret,
            secure=False
        )
        print("getting here")
        found = self.client.bucket_exists(settings.miniobucket)
        print(f'Bucket was found {found}')
        if not found:
            self.client.make_bucket(settings.miniobucket)
        else:
            print(f'Bucket {settings.miniobucket} exists!')
        
        self.settings = settings

    def store_png(self, file: UploadFile) -> any:
        file_id = uuid4()
        response = self.client.put_object(
            bucket_name=self.settings.miniobucket,
            object_name=f'{file_id}.{file.filename.split(".")[-1]}',
            data=file.file,
            length=file.size
        )
        return response


minio = None

def connect_minio():
    print("RUNNING connect to minio")
    global minio
    minio = MinioUtil()

def get_client():
    return minio
    