import json
import os
from typing import Optional
import requests
from pydantic import BaseModel

from structify.api import API_ENDPOINTS

ENDPOINT = (
    os.environ["STRUCTIFY_ENDPOINT"]
    if "STRUCTIFY_ENDPOINT" in os.environ
    else "https://api.structify.ai"
)


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


    def __getattr__(self, key: str):
        endpoint_cls = API_ENDPOINTS.get(key)
        if endpoint_cls is None:
            raise AttributeError(f"Unknown endpoint {key}")
        return endpoint_cls(self.token)


def login(email: str, password: str) -> Client:
    global AUTH_TOKEN
    result = requests.post(
        f"{ENDPOINT}/auth/login/", json={"email": email, "password": password}
    )
    AUTH_TOKEN = result.json()["token"]
    return AUTH_TOKEN
