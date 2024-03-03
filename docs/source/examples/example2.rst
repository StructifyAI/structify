Structifying Documents
=======================
In this tutorial, we've cover how you can use the Structify API to structure information from documents into datasets.
In the end, we'll show you how to implement this into an alternative to using RAG to query documents.

Extracting Company Information from Pitch Decks
-----------------------------------------------
This example will walk through the process of uploading pitch decks and extracting the company name, industry, founders, investors, and funding amount from each deck.

.. _document-example:

Step 1: Upload the Relevant Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we have to blueprint the schema of the dataset that we are interested in creating from these documents.
In this example, we will use the LLM generate method to create a dataset schema that will be used to structure the information from the pitch decks.

.. code-block:: python

    # You're going to want to get some sort of prompt describing the dataset to pass to the LLM
    # This can be hard coded or a user input, if you want to get fancy
    prompt = "Create a dataset schema for grabbing information from pitch decks such as the company name, industry, founders, investors, and funding amount."

    # Create the dataset schema
    pitchdecks = client.datasets.llm-create(prompt=prompt)

    # If you want to view the schema, you can do so by calling the view method
    await pitchdecks.status() == "complete"
    view = client.dataset.schema.view(name = pitchdecks.name)
    print(view)

.. note:: 
    If you want to edit the LLM-generated schema, you can use the dataset schema modify endpoint to do so.

Step 3: Populate the Dataset using the Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have the dataset schema, we can populate the dataset with the information from the pitch decks.

.. code-block:: python

    agent = client.agents.create(
        dataset = pitchdecks.name, 
        document_paths = ["newpath/deck1.pdf", "newpath/deck2.pdf"]
    )
    Structify.it(pitchdecks.name)

Step 4: Query the Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's assume you have a user that wants to search through the documents. 
Once you've used the populate method to create the dataset, you can use the query method to search through the documents.

.. code-block:: python

    def query_pitchdecks(query):
        response = client.analysis.query(dataset = pitchdecks.name, query = query)
        while response.status != "complete":
            response = client.analysis.query.retrieve(response.id)
            time.sleep(5)
        print(response)

    query_pitchdecks("Who are the investors in ABC Corp?")
    query_pitchdecks("What is the industry of XYZ Inc?")


Answering User Questions Based Off Documents
--------------------------------------------

This tutorial walks through the an implementation of functions based off the Structify API that take user queries and return relevant information from documents they've uploaded.

Step 1: Pass through Relevant Documents to Structify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, you'll want to upload the documents to Structify that the user wants to query.

.. code-block:: python

    from structifyai import Structify
    import time
    import asyncio
    client = Structify()

    # Assume you pass the user documents into a JSON (document_array) containing the file paths and the new desired Structify paths
    async def upload_documents(document_array):
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

        # Now, we want to store an array with the new file paths
        new_paths = []
        for document in document_array["documents"]:
            new_paths.append(document["structify_path"])

        return new_paths

Step 2: Process the User Query as a Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, you'll want to create a dataset schema based off the user query. This will involve using the LLM generate method to create a dataset schema that will be used to structure the information from the documents.

.. code-block:: python

    def create_dataset_schema(user_query):
        # You're going to want to get some sort of prompt describing the dataset to pass to the LLM
        # This is a simple implementation, but you could create an LLM function that transforms a user query into a dataset schema.
        # Or in the case of having datasets already created and refreshed, you could use an LLM tool choice function to determine which dataset to rely upon.
        prompt = "Create a dataset schema for answering the following questions: " + user_query

        # Create the dataset
        dataset = client.datasets.llm-create(prompt=prompt)

        # If you want to view the schema, you can do so by calling the view method
        await client.dataset.status(name = dataset["name"]) == "complete"
        view = client.datasets.schema.view(name = dataset["name"])
        print(view)

Step 3: Populate the Dataset using the Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have the dataset schema, we can populate the dataset with the information from the documents.

.. code-block:: python

    async def populate_dataset(document_array, user_query):
        uploads = await upload_documents(document_array)
        dataset = create_dataset_schema(user_query)
        agent = client.agents.create(
            name = dataset, 
            source = Documents.from_files(uploads)
        )
        Structify.it(dataset)

        # We have to wait for the dataset to be populated
        await Structify.it.status(name = dataset) == "complete"
        print("Dataset populated")

Step 4: Answer the User Query
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Finally, we can use the query method to search through the documents and return the relevant information to the user. Here, we use the `client.analysis.query` method to answer the user query, but through more complex implementations, you could use the `client.dataset.view` or `client.dataset.query` methods to return the relevant information.

.. code-block:: python

    answer = client.analysis.query(name = dataset, query = user_query)
    while answer.status != "complete":
        answer = client.analysis.query.retrieve(answer.id)
        time.sleep(5)
    print(answer)

And now you have output the answer to the user's question based off the documents they've uploaded. 


