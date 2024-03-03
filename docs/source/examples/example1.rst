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
    schema["name"] = "Board Members"
    schema["description"] = "Dataset containing information about board members of private companies in the technology sector."

    # Now, we will create a dataset with the schema
    board_members = client.datasets.create(schema)

    # Here, we're populating the dataset with the existing information
    client.agents.create(
        name = "Board Members",
        sources = Documents.from_files[path/to/your/board_members_dataset]}
    )
    Structify.it("Board Members")

.. note::
    We recommend only creating one agent to populate the dataset from documents. 

Step 3: Set Up Regular Refreshes of the Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have a dataset to store the board members information, we want to set up regular refreshes of the dataset to keep the information up to date.

.. code-block:: python

    # After getting the data from the uploaded CSV, we want to get the most recent information from the Internet sources.
    client.agents.create(
        name = "Board Members",
        sources = [Internet.SECFILINGS, Internet.PRESSRELEASES, Internet.COMPANYWEBSITES],
        number = 10
    )

    # We will set up a refresh schedule to run every week at 9:30am
    client.dataset.refresh(
        name = "Board Members", 
        id = agent_ids, # Make sure to grab the ids of the agents you created to populate the dataset
        type = "recurring",
        frequency = "weekly",
        time = "2024-04-01 09:30:00")


Step 4: Grab the Source of the Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have set up the dataset to be refreshed regularly, we want to be notified with the source attributed to any changes that occur. We can do this by setting up a notification that returns a backsource:

.. code-block:: python

    async def create_backsourced_notification(dataset_name, notification_details):
        notification = client.notification.create(name=dataset_name, json=notification_details)

        while True:
            notification = client.notification.view(name=dataset_name, id=notification.id)
            if notification.status == "processed":
                change = client.notification.view(name=dataset_name, id=notification.id)
                return client.analysis.backsource(name=dataset_name, target=change)
            time.sleep(5)


With this setup, you will be able to keep track of the board members of various private companies in the technology sector, and get notified with a source when that information changes such as board members starting or leaving posts.