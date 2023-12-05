import requests
import base64
from pathlib import Path
from dataclasses import dataclass

from structify.endpoint import ENDPOINT

@dataclass
class Document:
    name: str
    contents: bytes

class DocumentAPI:
    def __init__(self, token):
        self.token = token

    def upload(self, name: str, document: bytes):
        result = requests.post(
            f"{ENDPOINT}/files/add",
            json={
                "name": name,
                "contents": base64.b64encode(document).decode('utf-8'),
            },
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return result.json()

    def upload_file(self, path: str):
        path = Path(path)
        with open(path, "rb") as f:
            return self.upload(path.name, f.read())

    def list_files(self):
        result = requests.get(
            f"{ENDPOINT}/files/list",
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return result.json()

    def get_file(self, file_id: str) -> Document:
        result = requests.get(
            f"{ENDPOINT}/files/download/{file_id}",
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        res = result.json()
        return Document(
            name=res["path"],
            contents=base64.b64decode(res["contents"]),
        )
    
    def delete_file(self, file_id: str):
        result = requests.delete(
            f"{ENDPOINT}/files/delete/{file_id}",
            headers={
                "Authorization": f"{self.token}",
                "Content-Type": "application/json",
            },
        )
        return result.json()


