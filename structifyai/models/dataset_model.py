# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, conint

class DatasetModel(BaseModel):
    """
    DatasetModel
    """
    description: StrictStr = Field(...)
    name: StrictStr = Field(...)
    version: conint(strict=True, ge=0) = Field(...)
    __properties = ["description", "name", "version"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DatasetModel:
        """Create an instance of DatasetModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DatasetModel:
        """Create an instance of DatasetModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasetModel.parse_obj(obj)

        _obj = DatasetModel.parse_obj({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "version": obj.get("version")
        })
        return _obj


