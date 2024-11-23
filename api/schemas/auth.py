from pydantic import BaseModel, EmailStr, constr
from typing import Annotated

class LoginSchema(BaseModel):
    email: EmailStr
    password: Annotated[str, constr(min_length=8)]

class SignupSchema(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20, pattern=r'^[A-Za-z0-9_]+')]
    email: EmailStr
    password: Annotated[str, constr(min_length=8, pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])')]