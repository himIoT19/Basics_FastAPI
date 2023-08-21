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

# When we declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@him.get("/")
async def root():
    return {"message": "Hello Himanshu"}


@him.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):  # The query is the set of key-value pairs that go after the ? in a URL, separated by & characters,
    # eg: http://127.0.0.1:8055/items/?skip=0&limit=10
    """

    :param skip: query param with a value of 0
    :param limit: query param with a value of 10
    :return:
    """
    return fake_items_db[skip: skip + limit]


@him.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    """
    We can define some query parameters as required, some as having a default value, and some entirely optional, eg:
    :param item_id: path parameter str
    In this case, there are 3 query parameters
    :param needy: a required str
    :param skip: an int with a default value of 0
    :param limit: an optional int
    :return:
    """
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


# @him.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     """
#     When we declare a default value for non-path parameters (for now, we have only seen query parameters), then it is not required.
#     If we don't want to add a specific value but just make it optional, set the default as None.
#     But when we want to make a query parameter required, we can just not declare any default value
#     eg: Here the query parameter needy is a required query parameter of type str.
#     If you open in your browser a URL like:
#     http://127.0.0.1:8000/items/foo-item --> error(As 'needy' is a required query parameter, you would need to set it in the URL)
#     http://127.0.0.1:8000/items/foo-item?needy=sooooneedy --> Will work
#     :param item_id:
#     :param needy:
#     :return:
#     """
#     return {"item_id": item_id, "needy": needy}


# @him.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     """
#     We can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.
#     And we don't have to declare them in any specific order. They will be detected by name
#     :param user_id:
#     :param item_id:
#     :param q:
#     :param short:
#     :return:
#     """
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item["q"] = q
#     if not short:
#         item["description"] = "This is an amazing item that has a long description"
#     return item


# @him.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):  # In this case, if we go to:
#     # eg: http://127.0.0.1:8000/items/foo?short=1 or http://127.0.0.1:8000/items/foo?short=True or http://127.0.0.1:8000/items/foo?short=true
#     # or http://127.0.0.1:8000/items/foo?short=on or http://127.0.0.1:8000/items/foo?short=yes
#     # or any other case variation (uppercase, first letter in uppercase, etc.),
#     # your function will see the parameter short with a bool value of True. Otherwise, as False.
#     item = {"item_id": item_id}
#     if q:
#         item["q"] = q
#     if not short:
#         item["description"] = "This is an amazing item that has a long description"
#     return item


# @him.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):  # The same way, we can declare optional query parameters, by setting their default to None
#     # eg: http://127.0.0.1:8000/items/1?q=python
#     return {"item_id": item_id, "q": q} if q else {"item_id": item_id}


# @him.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


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


# Using an option directly from Starlette you can declare a path parameter containing a path using a URL like: /files/{file_path:path}
@him.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
