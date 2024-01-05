"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import os
import pandas as pd
from human import Human
from structify import Client
from structify.orm.value_types import UniqueText


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])

    client.kg.create(name="acme", description="Test use case")

    df = pd.read_csv("acme.csv")
    for i, (name, title, company) in df.iterrows():
        if i >= 2:
            break
        print(f"Adding {name} to the KG with values {title} and {company}")
        if pd.isna(company):
            continue
        client.entities.add(
            entity=Human(
                name=UniqueText(value=name),
                last_known_job_title=UniqueText(value=title),
                last_known_job=UniqueText(value=company),
            ),
            name="acme",
        )


if __name__ == "__main__":
    main()
