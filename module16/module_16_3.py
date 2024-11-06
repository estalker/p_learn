import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}'")
async def post_user(username: Annotated[
    str, Path(..., description="Enter username", min_length=5, mx_length=20, example="UrbanUser")],
                    age: Annotated[int, Path(..., description="Enter age", ge=18, le=120, example=24)]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(..., description="Enter user_id", ge=1, le=9999, example=1)],
                      username: Annotated[str, Path(..., description="Enter username", min_length=5, mx_length=20,
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(..., description="Enter age", ge=18, le=120, example=24)]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"

    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(..., description="Enter user_id", ge=1, le=9999, example=1)]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
