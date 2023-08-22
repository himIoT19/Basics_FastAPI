from pydantic import BaseModel


# region MODELS

# region Item : Create our data model
class Item(BaseModel):
    """
    Created our data model --> Item
    Then we declare our data model as a class that inherits from BaseModel.
    Use standard Python types for all the attributes

    For example, this model above declares a JSON "object" (or Python dict) like:
    1. {
            "name": "Foo",
            "description": "An optional description",
            "price": 45.2,
            "tax": 3.5
        }

    As description and tax are optional (with a default value of None), this JSON "object" would also be valid:
    1. {
            "name": "Foo",
            "price": 45.2,
        }
    """
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# endregion

# endregion
