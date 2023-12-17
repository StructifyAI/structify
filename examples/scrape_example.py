"""
This is an example of updating all your contacts from a CSV with
publically available information.
"""
import os
from structify import Client


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    schema = client.schemas.get(schema_name="Company")
    breakpoint()
    client.researcher.on_demand_scrape(
        query="Find AI companies", schema=[schema]  # pages=1_000,
    )


if __name__ == "__main__":
    main()
