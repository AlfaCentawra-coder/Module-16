from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            ge=1,
            le=100,
            example=1
        )
    ]
):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=5,
            max_length=20,
            example="UrbanUser"
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=18,
            le=120,
            example=24
        )
    ]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)