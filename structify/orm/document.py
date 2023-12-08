import base64
from typing import Optional
from pydantic import BaseModel


class Document(BaseModel):
    """
    Our wrapper around the document.
    """

    name: str
    contents: Optional[bytes] = None
    id: Optional[int] = None

    def to_dict(self):
        return {
            "name": self.name,
            "contents": base64.b64encode(self.contents).decode("utf-8"),
        }
