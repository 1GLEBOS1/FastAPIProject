from pydantic import BaseModel, EmailStr

class UsersBase(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str

class User(UsersBase):
    pass

class UserCreate(UsersBase):
    name: str
    email: EmailStr
    password: str

class UserRead(UsersBase):
    id: int

class UserUpdate(UsersBase):
    name: str
    email: EmailStr
    password: str

class UserDelete(BaseModel):
    id: int
