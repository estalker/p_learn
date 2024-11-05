import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user_number(user_id: Annotated[int, Path(..., description="Enter User ID", ge=1, le=100, example=1)]) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def get_user_info(username: Annotated[str, Path(..., description="Enter username", min_length=5, mx_length=20, example="UrbanUser")],
                        age: Annotated[int, Path(..., description="Enter age", ge=18, le=120, example=24)]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)