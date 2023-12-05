"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import os
from pydantic import BaseModel

from structify import Client


class Person(BaseModel):
    name: str
    current_title: str
    current_organization: str


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])

    # Create the schema we wish to use for this project
    # We could also grab an existing schema from the API.
    schema_info = client.schemas.create(
        "Person",
        "Describes a person, their associated title, and their organization",
        Person,
    )

    # Upload our seed data.
    kg = client.documents.upload_sync("test.csv", schema_info)

    # Update the KG with the new information
    client.kg.update_scrape(kg)

    # Export the KG into a format that can be used by other tools
    client.agent.structured_export(
        conditioning="Export these into the format", schema=Person
    )


if __name__ == "__main__":
    main()
