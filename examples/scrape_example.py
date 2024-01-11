import os
from structify import Client


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    entity = client.researcher.on_demand_scrape(
        query="Output the person who runs remote first capital.",
        schema_name="Human",
    )
    print(entity)


if __name__ == "__main__":
    main()
