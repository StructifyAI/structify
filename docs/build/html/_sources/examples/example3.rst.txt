Custom Tagging and Filtering Your Datasets
==========================================
Using the Structify API, you can enable analysis on top of your datasets. In this tutorial, we walk you through the steps of a simple analysis workflow such as finding and tagging contacts in your network based on certain domain expertise.

Finding and tagging contacts in your network
--------------------------------------------

In this tutorial, we will walk you through the steps of finding people in your network based on certain domain expertise.
For example, you might be curious to know who you know that has experience in the field of "AI Infrastructure" or "Beauty and Apparel".
Or you could want to know who in your network has experience in "Python" or "Sales".
With Structify, getting this information has never been easier.

Step 1: Create a Network Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, you are going to want to initialize a dataset to represent your network. You first do this by defining the schema for the dataset. 
The schema is a JSON object that defines the structure of the dataset. Remember that you are going to need to include a description for each entity, table, and column.

.. code-block:: python

    from structify import Structify
    from pydantic import BaseModel
    from typing import List, Optional
    import asyncio
    client = Structify()

    # Define the schema for the dataset in a Pydantic model

    class Person(BaseModel):
        name: str
        jobs: List[Job]
        education: List[School]
        photo: Optional[str]
        linkedin_url: str

    class Job(BaseModel):
        title: str
        company: str
        industry: str

    class School(BaseModel):
        name: str
        degree: str
        gradyear: int   


    # Create a network dataset
    network = client.dataset.create(
        name = "my_network",
        description = "A dataset representing the job and educational experience of people in my network",
        tables = [Person.schema(), Job.schema(), School.schema()]
    )

.. note:: 
    You can also use client.dataset.llm-create(prompt) to have our LLM generate your schema for you.

Step 2: Populate the Network Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, you are going to use the populate endpoint to add data to the dataset. Here, we use the scraper endpoint to grab the data from the Web.
Since information about your network can easily be found via LinkedIn, we are going to limit the sources to LinkedIn.
There are other limitations you can put in place such as limiting the tables you want to grab information for.
In this example, we don't care about where the person went to school, so we are going to limit the tables to just the jobs and person table.
Limiting where applicable is a good practice to save your credits.

.. code-block:: python

    # Populate the network dataset
    scraper = client.agents.create(
        dataset = "my_network",
        sources = [Source.Internet(websites = "linkedin.com"), Source.Document(path = "contacts.csv")],
        # Limit the number of active agents running to grab this information to 3, another form of limiting. The more agents, the faster the query will process.
        number = 3,
        tables = [Job, Person]
    )
    client.it("my_network")

    # Wait for the agents to finish processing 1000 contacts
    client.dataset.wait(name = "my_network", k = 1_000)
    print("The network dataset has finished populating from LinkedIn.")

Step 3: Search the Dataset for Contacts with Domain Expertise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that you have a dataset that represents your network, you can use the various endpoints to find contacts with domain expertise.
There are two main ways to do this:

**Option A: Direct Search**
If you've defined the schema with defined industries, you can use the view endpoint to find contacts who have worked at companies with a specific industry.

.. code-block:: python

    # Search for contacts who have worked at companies in the target industry
    aiInfra_contacts = client.dataset.view(
        name = "my_network",
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
    sales_contacts = client.analysis.filter(
        name = "my_network",
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to ensure the dataset is up to date, use the refresh endpoint to update the dataset with the latest information from the Web.

.. code-block:: python

    # Refresh the network dataset
    refresh = client.dataset.refresh(
        name = "my_network",
        id = scraper.id,
        # You can also specify the frequency of the refresh. The below will refresh the dataset every day at 9am.
        type = recurring,
        frequency = "daily",
        time = "2024-04-01 09:00:00"
    )

.. note:: 
    You will also want to make sure that you run the tagging again on the updated data each time the dataset completes a refresh.

