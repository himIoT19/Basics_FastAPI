from fastapi import FastAPI

mash = FastAPI()


@mash.get("/")
async def root():
    return {"message": "Hello Manansh"}


@mash.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@mash.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@mash.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@mash.get("/users")
async def read_users():
    return ["Rick", "Morty"]

# It will not be counted : The first one will always be used since the path matches first.
# @mash.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]
