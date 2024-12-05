from pydantic import BaseModel


class UserSignUp(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class CreateUpdatePost(BaseModel):
    title: str
    content: str
