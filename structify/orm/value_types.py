from enum import Enum
from pydantic import BaseModel


class IdNumber(BaseModel):
    value: int


class UniqueText(BaseModel):
    value: str


class ValueType(Enum):
    IdNumber = "IdNumber"
    UniqueText = "UniqueText"


CONVERTER = {IdNumber: "IdNumber", UniqueText: "UniqueText"}
