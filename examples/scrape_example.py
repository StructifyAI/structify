import os
from human import Human
from structify import Client
from structify.orm import Schema


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    entity = client.researcher.on_demand_scrape(
        query="Find me today's news articles that mention?",
        schema_name="Human",
    )
    print(entity)


if __name__ == "__main__":
    main()
