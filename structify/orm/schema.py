import json
from typing import List, Optional, Type, Union
from pydantic import BaseModel
from structify.orm.value_types import UniqueText, IdNumber, ValueType


class Property(BaseModel):
    name: str
    description: str
    value_type: ValueType

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "value_type": self.value_type.value.__name__,
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
    """
    A definition of a type of entity.
    """

    name: str
    description: str
    properties: List[Property]
    relationships: List[Relationship]
    version: Optional[int] = 1

    def to_dict(self: Optional["Schema"] = None):
        """
        This can be called both on an instance of the object,
        or on the class itself.
        """
        return {
            "name": self.name.strip(),
            "description": self.description.strip(),
            "version": self.version,
            "properties": [x.to_dict() for x in self.properties],
            "relationships": [x.to_dict() for x in self.relationships],
        }

    def from_pydantic(pydantic_model: Type[BaseModel]) -> "Schema":
        properties = []
        for field_name, field in pydantic_model.model_fields.items():
            property = Property(
                name=field_name,
                description=field.description,
                value_type=ValueType(field.annotation),
            )
            properties.append(property)

        # TODO: Assuming no relationships are defined in the Pydantic model
        relationships = []

        schema = Schema(
            name=pydantic_model.__name__,
            description=pydantic_model.__doc__ or "",
            properties=properties,
            relationships=relationships,
        )
        return schema


class SchemaInstance(BaseModel):
    """
    The superclass to inherit from when defining a schema.
    """
    kg_name: Optional[str] = None

    def to_dict(self):
        """
        Serialize an entity to be added.
        """
        return {
            "data": self.model_dump(),
            "kg_name": self.kg_name,
            "schema_name": self.__class__.__name__,
        }
