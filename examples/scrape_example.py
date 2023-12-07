"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import json
import os
import pandas as pd
from pydantic import BaseModel
from structify import Client
from structify.orm import Schema


class Person(BaseModel):
    name: str
    # current_title: str
    # current_organization: str


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])

    df = pd.read_csv("test2.csv", names=["name"])
    for _, row in df.iterrows():
        try:
            print(
                client.agent.scrape(
                    query=f"Can you find the linkedin and then the work history of '{row['name']}'? The '## refers to their Phillips Academy Andover class year."
                )
            )
        except:
            print(f"Error with {row['name']}")

    # schema = Schema(
    #     name="Person",
    #     description="Describes a person, their associated title, and their organization",
    #     schema_obj=Person,
    # )
    # client.schemas.add(schema)

    # for _, row in df.iterrows():
    #     person = Person(name=row["name"])
    #     client.entities.add(schema_name=schema.name, data=json.dumps(person.model_dump()))

    # kg = client.kg.process_document(document=uploaded_doc.id)

    # while kg.is_processing:
    #     kg = client.kg.get(kg.id)

    # # Update the KG with the new information
    # kg_aug = client.kg.update_scrape(kg, max_pages=1_000)

    # # Export the KG into a format that can be used by other tools
    # client.agent.structured_export(kg_aug, schema=Person)


if __name__ == "__main__":
    main()
