import io
from pydantic import BaseModel
from structifyai import Client


class Company(BaseModel):
    name: str
    website: str


def main():
    client = Client(host="http://localhost:8080")
    client.token = "test_token"
    client.documents.upload(body=io.BytesIO(b"sadf"))


if __name__ == "__main__":
    main()
