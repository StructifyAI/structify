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

In this tutorial, we will walk you through the steps of finding people in your network based on certain domain expertise.
For example, you might be curious to know who you know that has experience in the field of "AI Infrastructure" or "Beauty and Apparel".
Or you could want to know who in your network has experience in "Python" or "Sales".
With Structify, getting this information has never been easier.

Step 1: Create a Network Dataset
----------------------------------------------
First, you are going to want to initialize a dataset to represent your network. You first do this by defining the schema for the dataset. 
The schema is a JSON object that defines the structure of the dataset. Remember that you are going to need to include a description for each entity, table, and column.

.. code-block:: python

    from structifyai import Structify
    import asyncio
    client = Structify()

    # Define the schema for the dataset via a JSON object
    # Remember that each dataset is made up of entities, each entity is made up of tables, and each table is made up of columns
    schema = {
        "name": "my_network",
        "description": "Create a dataset named 'my_network' that tells me about the career and education experience of everyone in my network.",
        "entities": [
            {
            "name": "person",
            "description": "Someone who is in my network",
            "tables": [
                {
                "name": "jobs",
                "description": "A collection of the job titles and companies that each employee worked at",
                "columns": [
                    {
                    "name": "title",
                    "description": "The name of the job the employee held",
                    "type": "TEXT"
                    },
                    {
                    "name": "company",
                    "description": "The name of the company the employee worked at",
                    "type": "TEXT"
                    }
                    {
                    "name": "industry",
                    "description": "The industry the company is in",
                    "type": "TEXT"
                ]
                },
                {
                "name": "education",
                "description": "A collection of the schools that each employee went to",
                "columns": [
                    {
                    "name": "school_name",
                    "description": "The name of the school",
                    "type": "TEXT"
                    },
                    {
                    "name": "school_gradyear",
                    "description": "The year the employee graduated",
                    "type": "INTEGER"
                    }
                ]
                },
                {
                "name": "profile",
                "description": "A collection of the profile information of each person",
                "columns": [
                    {
                    "name": "name",
                    "description": "The name of the person",
                    "type": "TEXT"
                    },
                    {
                    "name": "photo",
                    "description": "The profile photo of the person",
                    "type": "IMAGE"
                    },
                    {
                    "name": "linkedin url",
                    "description": "The LinkedIn URL of the person",
                    "type": "URL"
                    }
                ]
                }
            ]
        ],
    }

    # Create a network dataset
    network = client.dataset.user_create(json=schema)
*Note that you can also use client.dataset.llm_create(text=prompt) to have our LLM generate your schema for you.*

Step 2: Populate the Network Dataset
----------------------------------------------
Next, you are going to use the populate endpoint to add data to the dataset. Here, we use the scraper endpoint to grab the data from the Web.
Since information about your network can easily be found via LinkedIn, we are going to limit the sources to LinkedIn.
There are other limitations you can put in place such as limiting the tables you want to grab information for.
In this example, we don't care about where the person went to school, so we are going to limit the tables to just the jobs and profile table.
Limiting where applicable is a good practice to save your credits.

.. code-block:: python

    # Populate the network dataset
    scraper = client.populate.scraperagent.create(
        dataset_name=network.name,
        sources=["linkedin"],
        number = 3 # Limit the number of active agents running to grab this information to 3, another form of limiting. The more agents, the faster the query will process.
        tables=["jobs", "profile"]
    )

    # Wait for the agents to finish running
    await scraper.status() == "complete"
    print("The network dataset has finished populating from LinkedIn.")

Step 3: Search the Dataset for Contacts with Domain Expertise
---------------------------------------------------------------------
Now that you have a dataset that represents your network, you can use the various endpoints to find contacts with domain expertise.
There are two main ways to do this:

**Option A: Direct Search**
If you've defined the schema with defined industries, you can use the view endpoint to find contacts who have worked at companies with a specific industry.

.. code-block:: python

    # Search for contacts who have worked at companies in the target industry
    aiInfra_contacts = client.dataset.view(
        dataset_name=network.name,
        # If you are looking for something with a certain value, you can specify it in a JSON like the following:
        inputs = {
            "entity": 
            {
                "name": "ANY",
                "tables": [
                    "name" : "jobs"
                    "column": [
                        "name" : "industry",
                        "value": ["AI Infrastructure", "Artificial Intelligence", "Machine Learning"]
                    ],
                ]
            }
        }

        # Then you can specify what you want to get back in your view in a JSON like the following:
        outputs = {
            "entity": 
            {
                "name": "ANY",
                "tables": [
                    "name" : "profile"
                    "columns": [
                        {
                            "name" : "name",
                        },
                        {
                            "name" : "linkedin url",
                        }
                    ],
                ]
            }
        }
    )

**Option B: Filtering**
You can also use the analysis filter endpoint to filter the dataset for contacts who have worked at companies with a industry.
This endpoint lets you filter for not specifically defined fields, such as "sales roles," for instance.

.. code-block:: python

    # Filter the dataset for contacts who have worked at companies in the target role
    sales_contacts = client.dataset.analysis.filter(
        dataset_name=network.name,
        # Here you specify that level of the dataset you are filtering through and where it is
        target_type = "column"
        target_location = {
            "entity": 
            {
                "name": "ANY",
                "tables": [
                    "name" : "jobs"
                    "column": [
                        "name" : "title",
                    ],
                ]
            }
        }
        filter_description = "any roles that are related to sales"
    )

Step 4: Regularly Refresh the Dataset
---------------------------------------------------------------------
If you want to ensure the dataset is up to date, use the refresh endpoint to update the dataset with the latest information from the Web.

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

With this setup, you will be able to keep track of the board members of various private companies in the technology sector, and get notified when that information changes such as board members starting or leaving posts.
