from structify import Client

import os
from typing import List
from pydantic import BaseModel

class Headlines(BaseModel):
    headlines: List[str]
    error: bool

client = Client(os.environ["STRUCTIFY_TOKEN"])

headlines: Headlines = client.scrape(f"What are some headline news articles from the nytimes today?", output=Headlines)
print(headlines)
