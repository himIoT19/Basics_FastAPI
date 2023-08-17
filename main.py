from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    """
    1. subclass that inherits from str and from Enum
    2. By inheriting from 'str' the API docs will be able to know that the values must be of type string and will be able to render correctly
    """
    # class attributes with fixed values, which will be the available valid values
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


him = FastAPI()


@him.get("/")
async def root():
    return {"message": "Hello Himanshu"}


@him.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@him.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@him.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@him.get("/users")
async def read_users():
    return ["Rick", "Morty"]


# It will not be counted : The first one will always be used since the path matches first.
# @him.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]


# create a path parameter with a type annotation using the enum class created (ModelName)
@him.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """

    :param model_name:
    :return:
    """
    # Compare enumeration members
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # Get the enumeration value -> your_enum_member.value (also access the value "lenet" with ModelName.lenet.value)
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
