Welcome to Structify!
=====================
We power you to collect, enrich, and update your own custom datasets using generative AI. Structify allows you transform any information from document to web page into structured data.

After reading our API documentation, you will be able to use our Python client to do things like:

* Create a personalized dataset representing the job history of everyone in your network
* Monitor changes in a dataset of real estate listings
* Extract structured data about startup financing events from a collection of SEC filings and pitch decks
* Automate notifications when a new job listing is posted that matches your criteria
* Analyze the sentiment of a collection of up-to-date social media noise about your company or your clients

...with the following three lines of code:

.. code-block:: python
   
   schema = "put your dataset schema here" # First, define the schema of your dataset as a library
   Structify.datasets.schema.user_create(name = "dataset_name", schema = schema) # Then, create a dataset frame
   Structify.datasets.create(name = "dataset_name", source = "The entire Internet") # Finally, add data to your dataset using our AI agents

It's that easy. Keep reading to learn more about how to use Structify to supercharge your team or an AI tool.

Get Started with Structify
--------------------------
.. toctree::
   :caption: Get Started
   :maxdepth: 1
   
   Overview <get_started/overview>
   Intro <get_started/intro>
   Quickstart <get_started/quickstart>


Check Out Our Capabilities
--------------------------
.. toctree::
   :caption: Guide
   :maxdepth: 1

   Creating Datasets <python_client/datasets>
   Searching Datasets <python_client/search>
   Using Documents <python_client/documents>
   Notifications <python_client/notifications>
   Analysis Tools <python_client/analysis>


Learn from Examples
-------------------
.. toctree::
   :caption: Tutorials
   :maxdepth: 2

   Making the Internet Your Database <examples/example0>
   Monitoring Changes in Datasets <examples/example1>
   Structifying Documents <examples/example2>
   Custom Tagging Your Datasets <examples/example3>
 

.. Indices and tables
.. -------------------
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

Read More
---------
.. toctree::
   :caption: More
   :maxdepth: 1

   API Reference <more/apiref>
   FAQ <more/faq>
   Changelog <more/changelog>
