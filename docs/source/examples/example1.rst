Monitoring Changes in Datasets
==============================
Using the Structify API, you can easily track changes in datasets over time and get notified when changes occur. This is helpful to keep up to date on information that changes frequently in large scale, such as company board members, executive team, or other personnel changes.

Tracking Private Company Board Members
--------------------------------------

In this tutorial, imagine you are intested in keeping tabs on who is on the board of various private companies.
Let's say furthermore, you are only interested in companies that are in the technology sector.
You want to know who is on the board of any given company, and you want to know when that information changes.

This information is not readily available, but you can determine it by periodically checking company websites, press releases, and SEC filings.
The goal being to regularly check if there have been any changes. Of course, since all the websites "Team" or "About Us" pages are all formatted differently, this is a near impossible scraping task to execute with high accuracy.

Structify dsirupts the manual processes in the status quo and allows you to easily collect this information to track any changes.

Step 1: Upload Your Existing Board Members Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we want to update the existing dataset that you may have. We start that process from the Structify document endpoint, using the upload call.

.. code-block:: python

    from structifyai import Structify

    # Here, we suppose that you have a dataset of board members in a CSV file
    # We will use the Structify API to upload this dataset to the platform
    csv_file_path = "path/to/your/board_members.csv"
    client.documents.upload(local = csv_file_path, structify_path = path/to/your/board_members_dataset)

    # Now, we want to wait for the document to be processed
    while True:
        document = client.documents.view(path = path/to/your/board_members_dataset)
        if document.status == "processed":
            break
        time.sleep(5)
    print("Document processed")

Step 2: Create a Structify Dataset for Board Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we will need to create a dataset to store the board members information. We can do this by defining the schema according to the uploaded CSV.

.. code-block:: python

    import pandas as pd

    # We will grab the schema from the uploaded CSV file
    df = pd.read_csv(client.documents.view(path = path/to/your/board_members_dataset))
    schema = df.dtypes.to_dict()

    # Now, we will create a dataset with the schema
    board_members = client.datasets.schema.user_create(
        name = "Board Members",
        description = "A dataset to store board members information for companies in the technology sector",
        schema = schema
    )

    # First, we're populating the dataset with the existing information
        client.datasets.create(
        name = "Board Members",
        sources = {"documents" : [path/to/your/board_members_dataset]}
        agent_number = 1
    )

Step 3: Set Up Regular Refreshes of the Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have a dataset to store the board members information, we want to set up regular refreshes of the dataset to keep the information up to date.

.. code-block:: python

    # After getting the data from the uploaded CSV, we want to get the most recent information from the Internet sources.
    client.datasets.create(
        name = "Board Members",
        sources = {"internet sources" :["press releases", "company websites", "SEC filings"]},
        agent_number = 10
    )

    # We will set up a refresh schedule to run every week at 9:30am
    client.dataset.refresh(
        name = "Board Members", 
        id = agent_ids, # Make sure to grab the ids of the agents you created to populate the dataset
        type = "recurring",
        frequency = "weekly",
        time = "2024-04-01 09:30:00")

