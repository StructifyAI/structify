import os
from human import Human
from structify import Client
from structify.orm import SchemaBox


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    client.schemas.delete(name="Company")
    client.schemas.delete(name="Human")
    client.schemas.add(schemas=SchemaBox.from_pydantic(Human))


if __name__ == "__main__":
    main()
