Structifying Documents
=======================
In this tutorial, we've cover how you can use the Structify API to structure information from documents into datasets.
In the end, we'll show you how to implement this into an alternative to using RAG to query documents.

This example will walk through the process of uploading pitch decks and extracting the company name, industry, founders, investors, and funding amount from each deck.

Step 1: Upload the Relevant Documents
--------------------------------------
Structify allows you to upload documents in a variety of formats, including PDFs, Word documents, and Powerpoint presentations.
We allow you to upload multiple documents at once, and you can specify the new path for each document.
We associate the documents with your account (or your user account), such that multiple datasets can be created from the same document 
(or sets of documents involving some of the same documents and different ones).

.. code-block:: python

    from structifyai import Structify
    import time
    import asyncio
    client = Structify()

    # You can upload multiple documents at once using a JSON containing the file paths and the new Structify paths
    document_array = {
        "documents" : [
            {
                "path" : "path/to/your/pitchdeck_abcCorp.pdf",
                "name" : "deck1",
                "structify_path" : "newpath/deck1.pdf",
            },
            {
                "path" : "path/to/your/pitchdeck_xyzInc.pdf",
                "name" : "deck2",
                "structify_path" : "newpath/deck2.pdf",
            }
        ]
    }

    try:
        uploads = client.documents.upload(paths=document_array)
        while uploads['status'] is Not "complete":
            uploads = client.documents.status(uploads.id)
            time.sleep(5)
        print("Uploads complete")
    except FileNotFoundError:
        print("File not found at path:", file_path)
    except Exception as e:
        print("An error occurred:", e)


Step 2: Create a Relevant Dataset
----------------------------------
Now, we have to blueprint the schema of the dataset that we are interested in creating from these documents.
In this example, we will use the LLM generate method to create a dataset schema that will be used to structure the information from the pitch decks.

.. code-block:: python

    # You're going to want to get some sort of prompt describing the dataset to pass to the LLM
    # This can be hard coded or a user input, if you want to get fancy
    prompt = "Create a dataset schema for grabbing information from pitch decks such as the company name, industry, founders, investors, and funding amount."

    # Create the dataset
    pitchdecks = client.datasets.llm_create(prompt=prompt)

    # If you want to view the schema, you can do so by calling the view method
    await pitchdecks.status() == "complete"
    view = client.datasets.schema.view(dataset_name = pitchdecks.name)
    print(view)
*Note: If you want to edit the LLM-generated schema, you can use the dataset schema modify endpoint to do so.*

Step 3: Populate the Dataset using the Documents
-----------------------------------------------
Now that we have the dataset schema, we can populate the dataset with the information from the pitch decks.

.. code-block:: python

    agent = client.populate.documentagent.create(
        dataset_name = pitchdecks.name, 
        document_paths = ["newpath/deck1.pdf", "newpath/deck2.pdf"]
    )

Step 4: Query the Documents
---------------------------
Now, let's assume you have a user that wants to search through the documents. 
Once you've used the populate method to create the dataset, you can use the query method to search through the documents.

.. code-block:: python

    def query_pitchdecks(query):
        response = client.dataset.analysis.query(dataset_name = pitchdecks.name, query = query)
        while response.status != "complete":
            response = client.dataset.analysis.query.retrieve(response.id)
            time.sleep(5)
        print(response)

    query_pitchdecks("Who are the investors in ABC Corp?")
    query_pitchdecks("What is the industry of XYZ Inc?")





