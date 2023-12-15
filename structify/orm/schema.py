import json
from typing import Any, List
from pydantic import BaseModel
from structify.orm.value_types import ValueType


class Property(BaseModel):
    name: str
    description: str
    value_type: ValueType

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "schema": json.dumps(self.schema_obj.schema()),
        }


class Relationship(BaseModel):
    name: str
    description: str
    relationship_type: str

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "schema": json.dumps(self.schema_obj.schema()),
        }


class Schema(BaseModel):
    name: str
    description: str
    properties: List[Property]
    relationships: List[Relationship]

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "schema": json.dumps(self.schema_obj.schema()),
        }
