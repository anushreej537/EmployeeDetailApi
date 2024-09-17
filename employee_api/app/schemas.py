from pydantic import BaseModel,EmailStr

class EmployeeBase(BaseModel):
    name : str
    email : EmailStr
    salary : float

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name : str = None
    email : EmailStr = None
    salary : float = None

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
