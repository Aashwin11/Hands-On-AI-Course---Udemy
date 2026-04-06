#Converting PYdantic Models to Dict, JSON is called Serialization

from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city: str
    pincode: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool=True

    createdAt: datetime
    address: Address
    tags: List[str]=[]

    model_config=ConfigDict(
        json_encoders={
            datetime:lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


user=User(
    id= 1,
    name="Aniket",
    email="a@gmail.com",
    createdAt=datetime(2024,3,15,14,30),
    address=Address(
        street="Walkins",
        city="California",
        pincode="53134a"
    ),
    is_active=True,
    tags=["premium User","Subsribver"]
)

python_dict=user.model_dump()
print(python_dict)
print("-------------------------------------------------")
print(f"User:{user}")


#Method 2

json_str=user.model_dump_json()
print("-------------"*5)
print(f"JSON STR: {json_str}")
