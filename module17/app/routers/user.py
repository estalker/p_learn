from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from module17.app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from module17.app.models import User, Task
from module17.app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
from module17.app.schemas import CreateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"

        )
    else:
        return user


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")
    else:
        tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
        return tasks


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values( username=create_user.username,
                                    firstname=create_user.firstname,
                                    lastname=create_user.lastname,
                                    age=create_user.age,
                                    slug=slugify(create_user.username)
                                    ))
    db.commit()
    return {"status_code": status.HTTP_201_CREATED,
            "transaction": "Successful"}


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")

    db.execute(update(User).where(User.id == user_id).values(
                                    username=update_user.username,
                                    firstname=update_user.firstname,
                                    lastname=update_user.lastname,
                                    age=update_user.age,
                                    slug=slugify(update_user.username)))

    db.commit()

    return {"status_code": status.HTTP_200_OK,
            "transaction": "User update is successful!"}


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

    db.execute(delete(Task).where(Task.user_id == user_id))

    db.execute(delete(User).where(User.id == user_id))

    db.commit()

    return {"status_code": status.HTTP_200_OK, "transaction": "User delete is successful!"}