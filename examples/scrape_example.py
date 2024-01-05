import os
from human import Human
from structify import Client
from structify.orm import Schema


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    # schema='{"title": "Board_member", "description": "Our representation of a board member", "type": "object", "properties": {"name": {"type": "string"}}}',
    client.researcher.on_demand_scrape(
        query="Who is the CEO of third500?",
        schema_name="Human",
    )


if __name__ == "__main__":
    main()
