from pydantic import Field
import os
import pandas as pd
from tqdm import tqdm

from structify.orm.schema import Schema, SchemaInstance
from structify.orm.value_types import UniqueText
from structify import Client


class AcmeHuman(SchemaInstance):
    """
    Description: AcmeHuman
    Version: 0
    """

    name: UniqueText = Field(description="The name of the person")
    employer: UniqueText = Field(description="The last known employer of this person")
    last_known_job_title: UniqueText = Field(
        description="The last known job title of the person"
    )
    link: UniqueText = Field(description="The link to the source of the information")


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    # client.schemas.add(Schema.from_pydantic(AcmeHuman))
    df = pd.read_csv("acme.csv")
    new_df = []

    results = []
    for _, name, job, org in tqdm(df.itertuples()):
        try:
            entity = client.researcher.on_demand_scrape(
                query=f"I know that {name} used to have the title of {job} at {org}. Where do they work now? Try to confirm we're talking about the same person.",
                schema_name="AcmeHuman",
            )
            results.append(entity)
            new_df.append(
                {
                    "name": entity[0].name,
                    "job": entity[0].last_known_job_title,
                    "org": entity[0].employer,
                    "link": entity[0].link,
                }
            )
        except Exception as e:
            print(e)

    new_df = pd.DataFrame(new_df)
    new_df.to_csv("acme_results.csv")


if __name__ == "__main__":
    main()
