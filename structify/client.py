from typing import Optional
import requests
from pydantic import BaseModel
import json

ENDPOINT = "http://localhost:8001"


class Client:
    def __init__(self, auth: str) -> "Client":
        self.token = auth

    def scrape(self, query: str, output: Optional[BaseModel] = None) -> BaseModel:
        schema = output.model_json_schema()
        payload = json.dumps({"query": query, "schema": json.dumps(schema)})
        result = requests.post(
            f"{ENDPOINT}/agent/scrape",
            data=payload,
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return output(**json.loads(result.json()))


def login(email: str, password: str) -> Client:
    global AUTH_TOKEN
    result = requests.post(
        f"{ENDPOINT}/auth/login/", json={"email": email, "password": password}
    )
    AUTH_TOKEN = result.json()["token"]
    return AUTH_TOKEN
