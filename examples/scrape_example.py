"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import os
from structify import Client
from structify.orm.value_types import UniqueText
from human import Human
import pandas as pd


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    df = pd.read_csv("acme.csv")
    for _i, (name, title, company) in df.iterrows():
        print(f"Adding {name} to the KG with values {title} and {company}")
        if pd.isna(company):
            continue
        client.entities.add(
            Human(
                kg_name="acme",
                description="Test description",
                name=UniqueText(value=name),
                last_known_job_title=UniqueText(value=title),
                last_known_job=UniqueText(value=company),
            ),
        )


if __name__ == "__main__":
    main()
