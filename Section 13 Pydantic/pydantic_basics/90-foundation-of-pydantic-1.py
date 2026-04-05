from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    is_active: bool


input_data={'id':101, 'name':"Chai_code",'is_active':True} #123

user=User(**input_data)
print(user)