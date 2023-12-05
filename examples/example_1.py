import os
from structify import Client

def main():
    client = Client(auth=os.environ["STRUCTIFY_TOKEN"])
    print(client.documents.upload_file("test_document.txt"))
    print(client.documents.list_files())

if __name__ == "__main__":
    main()
