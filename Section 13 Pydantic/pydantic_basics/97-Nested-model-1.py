from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class User(BaseModel):
    id: int
    name: str
    address: Address # User contains refernce of Address model



address=Address(

    street='Walkins Street',
    city='Boston',
    pincode='51324-Az'
)

user=User(
    id=123,
    name="Aniket",
    address=address
)

#other way
user_Data={
    "id":1,
    "name":"Aniket",
    "address": {
        "street":"Walkins Street 2",
        "city":"Texas",
        "pincode":"54212ER"
    }
}

user2=User(**user_Data)

print(user2)