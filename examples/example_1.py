import os
from structify import Client


def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    print(client.documents.upload_file("test_document.txt"))
    listed_files = client.documents.list_files()
    file_id = listed_files["files"][0][0]
    print(client.documents.get_file(file_id))


if __name__ == "__main__":
    main()
