from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDb, UserPublic, UserSchema, UserList

app = FastAPI()

database = []


@app.get("/", status_code=200, response_model=Message)
def read_root():
    return {"message": "Olá Mundo!"}


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": database}


@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="User not found")
    user_with_id = UserDb(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id
    return user_with_id
