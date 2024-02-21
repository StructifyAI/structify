Welcome to Structify!
========================================

Introduction
------------

In reading the Structify API docs, you've taken your first step towards data independence! 
By using the API, you will see how you can automatically source datasets, structure information, and run analytics. 
This documentation will guide you through the process of using the Structify API to access, create, and manipulate your data.
Soon, you will see how much fun it is to be structifying your data. 
We have a python client library, and a `Rest API </rest_docs>`_


Let's get started!

First, install the python client library using pip:
.. code-block:: bash

   pip install structifyai

.. code-block:: python

   from structifyai import Structify
   client = Structify()
   client.datasets.list()

.. toctree::
   
   Getting Started <getting_started>


Endpoints
------------
.. toctree::
   :caption: Endpoints
   :maxdepth: 1

   python_client/server
   python_client/datasets
   python_client/documents

Tutorials
------------
.. toctree::
   :caption: Tutorials

   Finding & Tagging Your Network <examples/example1>
   Structifying Documents <examples/example2>


Indices and tables
-------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :caption: Further Reading
