import os
from human import Human
from structify import Client
from structify.orm import Schema


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    try:
        client.schemas.get(name="Human")
        client.schemas.delete(name="Human")
    except Exception as e:
        print(f"Schema didn't already exist: {e}")
    client.schemas.add(Schema.from_pydantic(Human))


if __name__ == "__main__":
    main()
