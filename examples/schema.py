import json
from pydantic import BaseModel
from structifyai import Client
from structifyai.models import Dataset


class Company(BaseModel):
    name: str
    website: str


def main():
    client = Client(host="http://localhost:8080")
    client.token = "test_token"
    client.dataset.create(
        Dataset(
            name="test",
            description="This is a test dataset.",
            schemas=[json.dumps(Company.schema())],
        )
    )
    print(client.dataset.info(name="test"))
    client.dataset.delete(name="test")


if __name__ == "__main__":
    main()
