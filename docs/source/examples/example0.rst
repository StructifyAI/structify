Making the Internet Your Database
=================================

The central feature of Structify is powering individuals like you to structure unstructured data on the web. It's a powerful tool that can transform the web into a database that's always up-to-date.

Grabbing Relevant Press & News about Clients
--------------------------------------------

In this example, let's say we have an ever updating list of clients, but we want to keep track of the latest press and news about them. We can use Structify to grab the latest press and news about our clients and keep it up-to-date.

Step 1: Define a Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~
First things first. We need a Structify dataset to store all this information. We create one by defining the schema.

.. code-block:: python

    from structifyai import Structify
    client = Structify()

    schema = {
        "name": "client_press",
        "description": "Create a dataset named client_press that stores all the information about press and social media noise relevant to them in a tables, with each entity being a different client of ours.",
        "tables": [
            {
                "name": "press",
                "description": "A collection of the outlets and articles that mention each client",
                "columns": [
                    {
                        "name": "title",
                        "description": "The headline of the article talking about our client",
                        "type": "TEXT"
                    },
                    {
                        "name": "outlet",
                        "description": "The name of the outlet that published the article",
                        "type": "TEXT"
                    }
                ]
            },
            {
                "name": "social_media_noise",
                "description": "A collection of what people are saying on social media about each client",
                "columns": [
                    {
                        "name": "app",
                        "description": "The social media app where the noise was posted, limited to either Twitter or Instagram",
                        "type": "ENUM"
                    },
                    {
                        "name": "social_media_handle",
                        "description": "The handle of the person who posted the social media noise",
                        "type": "TEXT"
                    },
                    {
                        "name": "content",
                        "description": "The text of the post",
                        "type": "TEXT"
                    }
                ]
            }
        ]
    }

    client.dataset.create(schema)

Step 2: Add Clients
~~~~~~~~~~~~~~~~~~~~
Now, we are going to manually define the entities of the dataset. We will add a few clients to the dataset using the `client.dataset.modify` endpoint.

.. code-block:: python

    client.dataset.modify(name = "client_press", edits = [
        {
            "action": "INSERT",
            "target": "entity",
            "values": [
                {
                    "name": "LeBron James",
                    "description": "A professional basketball player for the Los Angeles Lakers"
                },
                {
                    "name": "Elon Musk",
                    "description": "The CEO of Tesla and SpaceX"
                },
                {
                    "name": "Taylor Swift",
                    "description": "Best-selling singer-songwriter worth over $1 billion"
                }
            ]
        }
    ])

Step 3: Grab Current Press & News
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now, we are going to use the Structify API to grab the latest press and news about our clients. We will use the `client.dataset.create` endpoint to do this.

.. code-block:: python

    # In creating agents to populate the dataset, we have to specify the dataset name, the sources, and the number of agents.
    client.agents.create(
        name = "client_press",
        sources = [Internet.NEWS, Internet.TWITTER, Internet.INSTAGRAM]
        number = 3)

    agent_ids = []
    for agent in client.dataset.get(name = "client_press")["agents"]:
        agent_ids.append(agent["id"])
    
    # We want to refresh this each morning, so we can stay up to date.
    client.dataset.refresh(
        name = "client_press", 
        id = agent_ids, 
        type = "recurring",
        frequency = "daily",
        time = "2024-04-01 06:15:00")

Step 4: Query the Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~
Now, we can query the dataset to see the latest press and news about our clients.

.. code-block:: python

    client.dataset.query(name = "client_press", query = {
        "tables": ["press", "social_media_noise"],
        "entities": ["LeBron James", "Elon Musk", "Taylor Swift"]
    })

And just like that, you will be able to stay on top of all the latest press about your clients.