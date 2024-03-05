Using Documents in Structify
============================
In many cases, a wealth of unstructured data lies within documents without set formats. Structify allows you to upload these documents and extract the data you need from them.

Uploading Documents
---------------------
You can upload documents to Structify using ``client.documents.upload`` and then specifying the old file path and the new file path. The new file path is the path where the file will be stored in Structify.

.. code-block:: python

    from structifyai import Structify
    structify = Structify()

    structify.documents.upload(local = old_file_path, remote = new_file_path)

You can also bulk upload documents by specifying the old file paths and the new file paths by specifying them in a dictionary and passing the dictionary as a parameter.

Once you've uploaded them, you can use our other document endpoints to list, view, modify, and delete the documents.

Currently, we support the following document formats:

- PDFs
- Images (JPG, PNG, etc.)
- Text files (TXT, CSV, etc.)

We are working to support more formats in the future, such as:

- Word documents (DOCX)
- Excel spreadsheets (XLSX)
- PowerPoint presentations (PPTX)

In the meantime, we recommend converting all your documents to either PDFs or images before uploading them to Structify.

.. 
    .. autofunction:: structifyai.operations.DocumentsOperations.delete
        :no-index:
    .. autofunction:: structifyai.operations.DocumentsOperations.download
        :no-index:
    .. autofunction:: structifyai.operations.DocumentsOperations.list
        :no-index:
    .. autofunction:: structifyai.operations.DocumentsOperations.upload
        :no-index:

.. _Structuring Documents:

Extracting Data from Documents
-------------------------------
Creating datasets from documents is quite simple. You just use the ``structify.agents.create`` method and specify the document file path or paths you want to include in the dataset.

.. code-block:: python

    structify.agents.create(name = "employees", source = Source.Document(path = new_file_path/*))])

And just like that you've created a dataset from your documents. You can then run our :doc:`analysis` tools on the dataset to extract the data you need.