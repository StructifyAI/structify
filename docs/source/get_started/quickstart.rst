.. _quickstart:

Quickstart Guide
================
Datasets on demand for you or your AI tool in three easy steps.

#. :ref:`Installation`
#. :ref:`Getting-An-API-Key`
#. :ref:`Create-Your-First-Dataset`

Our documentation will guide you through the process of using the Structify API to access, create, and manipulate your data.
When you create a dataset, Structify spins up AI agents to populate your custom schema by indexing information from the sources you specify. Soon, you will see how much fun it is to "structify" your data. 
We have a python client library, and we are working on releasing a `Rest API </rest_docs>`_.

.. _Installation:

Installation
------------

Let's get started!

First, install the python client library using pip:

.. code-block:: bash

   pip install structifyai


Running ``pip list`` after it completes will show you the Python libraries you've got, which will let you know if the Structify Python library was successfully installed.

Anytime you want to use the Structify Python library, you'll need to import it:

.. code-block:: python

   from structifyai import Structify
   client = Structify()


.. _Getting-An-API-Key:

Getting an API Key
------------------
We are early, so it is important to us to develop a relationship with all our users. That said, the quickest way to secure an API key is to `email us <mailto:team@structify.ai>`_ with your name, email, and a brief description of your use case. We will send you back an API key and your account details.

Alternatively, you can book a time for a detailed guided tour of our API and get an API key at the end of the session. Please find a time to meet via `our Calendly <https://calendly.com/ronakgandhi/structify-demo>`_.

Once you have your API key, you can use it to authenticate your requests to the Structify API. You can do this by setting the ``api_key`` attribute of the client object:

Our API recognizes two types of users: business and personal. Both have organizations and users underneath, for the case that you are letting users of your program make API calls through us. Every one of the endpoints is done through an authenticated personel.

.. _create-your-first-dataset:

Create Your First Dataset
-------------------------
You can create a dataset with two quick successive API calls:

#. Define a schema using ``client.dataset.schema.user_create`` or ``client.dataset.schema.llm_create``.
#. Specify the source to populate the dataset from with ``client.dataset.create``.

Here's an example of how you would make an API call to create a dataset:

.. code-block:: python
   
   from structifyai import Structify
   client = Structify()

   # Define a schema
   schema = {
      "name": "books",
      "description": "Create a dataset named 'books' that tells me about the authors and publishers of books.",
      "entities": [
         {
         "name": "book",
         "description": "A text with both an author and a publisher",
         "tables": [
               {
               "name": "author",
               "description": "A collection of information about the authors of the book",
               "columns": [
                  {
                  "name": "name",
                  "description": "The name of the author(s)",
                  "type": "TEXT"
                  },
                  {
                  "name": "genre",
                  "description": "The genre that the author most often writes in",
                  "type": "TEXT"
                  }
               ]
               },
               {
               "name": "publisher",
               "description": "A collection of information about the publisher of the book",
               "columns": [
                  {
                  "name": "name",
                  "description": "The name of the publisher",
                  "type": "TEXT"
                  },
                  {
                  "name": "location",
                  "description": "where the publisher is located",
                  "type": "TEXT"
                  }
               ]
               },
               {
               "name": "details",
               "description": "A collection of the details of the book",
               "columns": [
                  {
                  "name": "name",
                  "description": "The name of the book",
                  "type": "TEXT"
                  },
                  {
                  "name": "cover",
                  "description": "The cover photo of the book",
                  "type": "IMAGE"
                  },
                  {
                  "name": "copies_sold",
                  "description": "The number of copies of the book sold to date",
                  "type": "INTEGER"
                  }
               ]
               }
            ]
         }
      ],
   }

   # Use the schema to create the dataset
   books_dataset = client.dataset.user_create(json=schema)

   #Specify the source to populate the dataset from
   source = {"source": "Internet", "specification": "https://www.goodreads.com/"}
   client.dataset.populate(books_dataset['id'], json=source)

.. tip::
   You could just as easily use the ``client.dataset.schema.llm_create`` method to create a dataset with a schema that is automatically generated from the description included in the example above.

With that, you are on your way to structifying your data.
