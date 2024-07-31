from typing import TypedDict

class MyDict(TypedDict):
    name: str
    age: int

my_dict: MyDict = {'name': 'John', 'age': 30}
