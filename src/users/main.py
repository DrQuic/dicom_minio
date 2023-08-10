from fastapi import APIRouter, Depends, Response
from src.users.dtos.user import User
from utils.minio import get_client, MinioUtil
from sqlalchemy.orm import Session
from db.connection import get_db_session
from src.users.models.user import User as UserDBModel
from utils.user import preparse_store_data

router = APIRouter()

@router.post("/")
async def store_user(
    user: User = Depends(preparse_store_data), 
    minio: MinioUtil = Depends(get_client), 
    db: Session = Depends(get_db_session)
):
    result_file= minio.store_png(user.profile_picture)
    user_db: UserDBModel = UserDBModel(
        name=user.name, 
        last_name=user.last_name, 
        age=user.age, 
        profile_picture=result_file.object_name
    )
    
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@router.get("/{id}")
async def get_user(
    id: int,
    db: Session = Depends(get_db_session)
):
    user: UserDBModel = db.query(UserDBModel).filter(UserDBModel.id == id).first()
    return user
