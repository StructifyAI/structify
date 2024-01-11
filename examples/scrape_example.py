import os
from structify import Client


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    entity = client.researcher.crawl(
        query="Find angel investors",
        schema_name="Human",
    )
    print(entity)


if __name__ == "__main__":
    main()
