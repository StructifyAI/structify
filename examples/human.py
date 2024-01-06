from pydantic import Field
from structify.orm.schema import SchemaInstance
from structify.orm.value_types import UniqueText


class Human(SchemaInstance):
    """
    Description: A Human
    Version: 1
    """

    name: UniqueText = Field(description="The name of the person")
    employer: UniqueText = Field(description="The last known employer of this person")
    last_known_job_title: UniqueText = Field(description="The last known job title of the person")
