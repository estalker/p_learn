import uvicorn
from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


@app.get("/")
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        user_index = [index for index in range(len(users)) if users[index].id == user_id][0]
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_index]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User is not found")


@app.post("/user/{username}/{age}")
async def post_user(username: Annotated[
    str, Path(..., description="Enter username", min_length=5, mx_length=20, example="UrbanUser")],
                    age: Annotated[int, Path(..., description="Enter age", ge=18, le=120, example=24)]) -> User:
    current_id = int(max(tuple(user.id for user in users), default=0)) + 1
    new_user = User(id=current_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(..., description="Enter user_id", ge=1, le=9999, example=1)],
                      username: Annotated[str, Path(..., description="Enter username", min_length=5, mx_length=20,
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(..., description="Enter age", ge=18, le=120, example=24)]) -> User:
    try:
        user_index = [index for index in range(len(users)) if users[index].id == user_id][0]
        user = users[user_index]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User is not found")


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(..., description="Enter user_id", ge=1, le=9999, example=1)]) -> User:
    try:
        user_index = [index for index in range(len(users)) if users[index].id == user_id][0]
        user = users.pop(user_index)
        return user
    except  IndexError:
        raise HTTPException(status_code=404, detail="User is not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
