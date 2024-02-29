Creating Datasets
=================

Overview
--------
Structify's API, at its core, is designed to let developers collect datasets on demand. You can create a dataset in just a few lines of code. This guide will walk you through the three main steps in getting your first custom dataset:

#. :ref:`define-schema`
#. :ref:`Populating-Datasets`
#. :ref:`Refreshing-Dataset`

.. _define-schema:

Defining Your Schema
---------------------
The basis of creating datasets is defining the schema, much like creating a blueprint for a database. The schema of a Structify dataset is comprised of entities, which are made of tables, which are in turn made up of columns. Check out the example under :ref:`user-schemas` for more clarity.

Before you can create researchers to automatically fill up your datasets, we need to define the schema of the dataset. Note that each entity, table, and column in the dataset need the following: name, description, and type. There are two ways to define the schema: using the LLM defined schemas or creating your own custom user defined schemas.

.. _user-schemas:

Custom User Defined Schemas
~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you have a schmea you want your dataset to follow, you can easily pre-define your schema in JSON.

.. code-block:: python
    
        from structifyai import Structify
        client = Structify()
    
        schema = {
            "name": "employees",
            "description": "Create a dataset named 'employees' that tells me about their job and education history.",
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
                }
            ]
        }
    
        employees = client.dataset.schema.user_create(schema)
        client.dataset.schema.view(employees)

And the output will echo back a JSON representation of the schema you just created.


LLM Defined Schemas
~~~~~~~~~~~~~~~~~~~
Instead of writing out an entire schema, you can input plain text to allow the LLM to define and create your schema.

Here's an example of an API call to create a dataset using the LLM and the response.

.. code-block:: python

    from structifyai import Structify
    client = Structify()

    prompt = {"text": "Create a dataset named 'employees' that tells me about their job and education history."}

    employees = client.dataset.schema.llm_create(prompt)
    print(employees)


And the output will look like this:

.. code-block:: json

    {
        "name": "employees",
        "description": "Create a dataset named 'employees' that tells me about their job and education history.",
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
            }
        ]
    }


.. tip::
    You can edit the schema that is returned if it is missing something you need. In that case, you can use ``client.dataset.schema.modify`` to adjust the schema.


.. _populating-datasets:

Populating Your Datasets
------------------------
Once you have blueprinted your dataset by creating a schema, you can now use Structify's research agents to collect data to fill your dataset.

For most datasets, you are going to want to user our scraper agents to collect data from the web. You can use ``client.dataset.create`` to populate a dataset with an initial batch of data. This API call requires the following:

- **name:** The name of the dataset you want to populate
- **source:** A description of the sources or types of sources you want the agent to use (e.g. “LinkedIn” or “news articles”)
- **agent_number:** The number of agents that are actively running for a query. The more you create, the faster the dataset will populate, but it requires more credits to do so.

Here's an example of an API call to populate that employees dataset with data from LinkedIn:

.. code-block:: python

    from structifyai import Structify
    client = Structify()

    client.dataset.create(name = "employees", source = "LinkedIn", agent_number = 5)

.. tip::
    You can check the status of the populate request through ``employees.status()`` or ``print(client.dataset.list("employees"))`` to see the status object.

Populating Datasets from Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sometimes, you will want to collect data from documents, such as PDFs or PNGs. You can use the ``client.dataset.create`` endpoint off of documents as well. 

We'll walk you through the process to uploading documents and such in the :doc:`documents` section. Or you can check out the tutorials at :ref:`document-example`.


Adjusting Credit Usage per Populate Request 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Populating datasets with Structify's research agents will be the main process that uses your credit allotment. There a few additional parameters you can add to an API call to limit the credit usage:

- **tables**: If you want the scraper to just grab information for a certain table (or tables), include the name to limit the scraping.
- **columns**: If you want the scraper to just grab information for a certain column, you can specify the column (or columns) name. *Note that this parameter only works if you first specify the tables.*
- **keywords:** Additional keywords or search terms to guide the research agent in finding relevant data on the web.
- **time_limit:** A set amount of time that the scraper should run for. This parameter is designed to limit your request to save credits, if needed.
- **source_limit:** A set amount of sources that the scraper will check. This parameter is designed to limit your request to save credits, if needed.

.. tip::
    Check ``client.account.credits_remaining()`` periodically to see how many credits you have left.

.. _Refreshing-Dataset:

Refreshing Your Dataset
-----------------------
Of course, the data in your dataset will become outdated over time. You can use the `client.dataset.refresh` API call to update the data in your dataset.

You can set the dataset to refresh one-time, on a recurring schedule, or refresh continuously. 

.. code-block:: python

    # First, you need to determine the id of the agents created for the dataset
    agents = client.dataset.agents.list("employees")
    agent_ids = [agent['id'] for agent in agents]

    # Then, you can refresh the dataset. Note, you could set the type to "recurring" or "continuous" if you want to refresh the dataset on a schedule or continuously.
    client.dataset.refresh(name = "employees", id = agent_ids, type = "one-time")

.. note::
    If you want to refresh the dataset on a schedule, you have to pass an additional time and frequency parameter to the API call. The time parameter is a string in the format "YYYY-MM-DD HH:MM:SS", where the date determine the start date and the time represents the time the refresh will run. The frequency parameter is a string that can be "daily", "weekly", "biweekly," "monthly", or "yearly".

Bonus: Sharing Datasets
-----------------------
Oftentimes, you will want to share your dataset with others. You can use the ``client.dataset.share`` API call to share your dataset with others. This API call requires the following:

* **name:** The name of the dataset you want to share
* **share_method:** The method of sharing the dataset. This can be "public" or "private". 
* **restrictions**: (optional) A list of restrictions that you want to place on the dataset. This can be "view-only", "refresh-only", "edit", "no-delete", or "admin". Each successive option has more priviledges. The default is "view".
* **users:** (optional) A list of user ids that you want to share the dataset with.
* **emails:** (optional) A list of emails that you want to share the dataset with.

.. note::
    If you want to share the dataset with specific users, you can use the "private" method and pass a list of either ``user_ids`` to the "users" parameter. If the target recipients are not users, you can pass a list of emails to the "emails" parameter, which will send them an email link to create an account and view the dataset.

Here's an example that walks through sharing the employees dataset with various co-workers who do not have Structify accounts:

.. code-block:: python

    from structifyai import Structify
    client = Structify()

    client.dataset.share(
        name = "employees", 
        share_method = "private", 
        restrictions = "no-delete",
        emails = ["ellie@structify.ai", "sami@structify.ai", "maya@structify.ai"])


.. These are all folded into the client. So just use
.. .. code-block:: python

   .. from structifyai import Client
   .. client = Client()
   .. client.datasets.create('my-dataset', 'my-dataset-description')
   .. client.datasets.list()
   .. client.datasets.info('my-dataset')
   .. client.datasets.query('my-dataset', 'my-query')
   .. client.datasets.delete('my-dataset')


