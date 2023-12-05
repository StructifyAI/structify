from typing import Optional
import requests
import base64
from pathlib import Path
from pydantic import BaseModel
import json

from structify.endpoint import ENDPOINT


class AgentAPI:
    def __init__(self, token):
        self.token = token

    def scrape(self, name: str, schema: Optional[BaseModel] = None):
        payload = {
            "query": name,
        }
        if schema:
            payload['schema'] = json.dumps(schema.model_json_schema())
        result = requests.post(
            f"{ENDPOINT}/agent/scrape",
            json=payload,
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return result.json()
