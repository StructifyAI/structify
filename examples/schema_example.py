import os
from structify import Client
from structify.orm import Schema
from human import Human

def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    try:
        _schema = client.schemas.get(name="Human")
        client.schemas.delete(name="Human")
    except:
        print("Schema didn't already exist")
    client.schemas.add(Schema.from_pydantic(Human))


if __name__ == "__main__":
    main()
