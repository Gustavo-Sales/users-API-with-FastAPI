from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Role(str, Enum):
    admin = 'admin'
    user = 'user'


class User(BaseModel):
    id: UUID = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: list[Role]


class UpdateUser(BaseModel):
    first_name: str | None
    last_name: str | None
    roles: list[Role] | None