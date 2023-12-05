import requests
import base64
from pathlib import Path

from structify.endpoint import ENDPOINT


class Schema:
    name: str
    contents: bytes


class SchemasAPI:
    def __init__(self, token):
        self.token = token

    def add(self, name: str, schema: bytes):
        """
        Adds a schema to the API.
        """
        result = requests.post(
            f"{ENDPOINT}/schemas/add",
            json={
                "name": name,
                "contents": base64.b64encode(schema).decode("utf-8"),
            },
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return result.json()
