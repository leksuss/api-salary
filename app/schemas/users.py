from pydantic import BaseModel, Field, EmailStr


class UserBaseSchema(BaseModel):
    email: EmailStr
    full_name: str


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(alias="username")
    password: str


class UserCreateSchema(UserBaseSchema):
    password: str = Field()


class UserResponse(BaseModel):
    access_token: str


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        from_attributes = True
