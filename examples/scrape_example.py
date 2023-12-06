"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import os
from pydantic import BaseModel

from structify import Client
from structify.orm import Document, KnowledgeGraph, Schema


class Person(BaseModel):
    name: str
    current_title: str
    current_organization: str


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])

    schema = Schema(
        name="Person",
        description="Describes a person, their associated title, and their organization",
        schema_obj=Person,
    )
    client.schemas.add(schema)

    # Upload our seed data.
    try:
        client.documents.delete(name="test.csv")
    except:
        print("No test.csv found")
        pass
    uploaded_doc = client.documents.add(
        Document(name="test.csv", contents=open("test.csv").read())
    )

    kg = client.kg.process_document(document=uploaded_doc.id)

    # while kg.is_processing:
    #     kg = client.kg.get(kg.id)

    # # Update the KG with the new information
    # kg_aug = client.kg.update_scrape(kg, max_pages=1_000)

    # # Export the KG into a format that can be used by other tools
    # client.agent.structured_export(kg_aug, schema=Person)


if __name__ == "__main__":
    main()
