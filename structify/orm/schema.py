from typing import List, Optional, Type
from pydantic import BaseModel
from structify.orm.value_types import CONVERTER, ValueType


class Property(BaseModel):
    name: str
    description: str
    value_type: ValueType

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "value_type": self.value_type.value,
        }


class Relationship(BaseModel):
    name: str
    description: str
    other: str

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "other": self.other,
        }


class SchemaBox(BaseModel):
    schemas: List["Schema"]

    def from_pydantic(pydantic_model: Type[BaseModel]) -> "Schema":
        """
        We have to make sure we also get all the connected classes.
        """
        schemas = []
        unprocessed_schemas = [pydantic_model]
        processed_schemas = set()
        while len(unprocessed_schemas) > 0:
            schema = unprocessed_schemas.pop()
            if schema in processed_schemas:
                continue
            for attribute in schema.model_fields.values():
                if issubclass(attribute.annotation, SchemaInstance):
                    unprocessed_schemas.append(attribute.annotation)
            schemas.append(Schema.from_pydantic(schema))
            processed_schemas.add(schema)

        return SchemaBox(schemas=schemas)

    def to_dict(self):
        return [x.to_dict() for x in self.schemas]


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
        relationships = []
        for field_name, field in pydantic_model.model_fields.items():
            if field.annotation in CONVERTER:
                property = Property(
                    name=field_name,
                    description=field.description,
                    value_type=CONVERTER[field.annotation],
                )
                properties.append(property)
            elif issubclass(field.annotation, SchemaInstance):
                # Relationship
                rel_cls = field.annotation
                relationships.append(
                    Relationship(
                        name=rel_cls.get_name(),
                        description=rel_cls.get_description(),
                        other=field.annotation.__name__,
                    )
                )
            else:
                raise Exception(f"Unknown type: {field.annotation}")

        description = pydantic_model.get_description()
        version = pydantic_model.get_version()

        schema = Schema(
            name=pydantic_model.__name__,
            description=description,
            version=version,
            properties=properties,
            relationships=relationships,
        )
        return schema


class SchemaInstance(BaseModel):
    """
    The superclass to inherit from when defining a schema.
    """

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__

    @classmethod
    def get_version(cls) -> int:
        return int(cls.__doc__.split("Version:")[1].split("\n")[0].strip())

    @classmethod
    def get_description(cls) -> str:
        return cls.__doc__.split("Description:")[1].split("\n")[0].strip()
