from structify import Client

from typing import List
from pydantic import BaseModel
import pandas as pd
from tqdm import tqdm


class Company(BaseModel):
    names: List[str]
    website_stem: str
    error: bool


class LinkedIn(BaseModel):
    url: str
    error: bool


client = Client("test_token")

df = pd.read_csv("test.csv", names=["name", "title", "company"])

linkedins = []

pbar = tqdm(df.itertuples(index=False))

for name, titls, company in pbar:
    company = client.scrape(f"What are {company} common names?", output=Company)
    added = False
    for company_name in company.names:
    # try:
        linkedin = client.scrape(
            f"Can you find the linkedin url of {name} who works at {company_name}?",
            output=LinkedIn,
        )
        # except:
        #     continue

        if not linkedin.error:
            pbar.set_description(f"Found linkedin for {name}")
            added = True
            linkedins.append(linkedin.url)
            break

    if not added:
        linkedins.append("")

df["linkedin"] = linkedins
df.to_csv("test_2.csv", index=False)