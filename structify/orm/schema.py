import json
from typing import Any
from pydantic import BaseModel


class Schema(BaseModel):
    name: str
    description: str
    schema_obj: Any

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "schema": json.dumps(self.schema_obj.schema()),
        }
