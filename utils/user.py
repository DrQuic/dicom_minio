from fastapi import Request
from src.users.dtos.user import User

async def preparse_store_data(request: Request) -> User:
    form = await request.form()
    profile_picture = form.get("profile_picture")
    user = User(name=form.get("name"), last_name=form.get("last_name"), age=form.get("age"), profile_picture=profile_picture)
    return user