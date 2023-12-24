import os
from pydantic import BaseModel, Field
from structify import Client
from structify.orm import Schema
from structify.orm.value_types import UniqueText, IdNumber
from . import human

def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    client.schemas.delete(name="Human")
    client.schemas.add(Schema.from_pydantic(human.Human))


if __name__ == "__main__":
    main()
