from typing import List,Dict,Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str=Field(
        ..., # indicates field is required
        min_length=3,
        max_length=50,
        description="Employee name",
        example="Hitesh"
    )

    department: Optional[str]='General'
    salary: float=Field(
        ...,
        ge=10000, #greater than or eequal to
        le=100000,
        description="Salary of general person"
    )

class User(BaseModel):
    email: str=Field(...,regex=r'')
    phone= str=Field(...,regex=r'')
    age: int=Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount: float=Field(
        ge=0,
        le=100,
        description="Discount percentage on items"

    )

