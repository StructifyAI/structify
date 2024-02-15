Dataset
-------------------
These are all folded into the client. So just use
.. code-block:: python

    from structifyai import Client
    client = Client()
    client.datasets.create('my-dataset', 'my-dataset-description')
    client.datasets.list()
    client.datasets.info('my-dataset')
    client.datasets.query('my-dataset', 'my-query')
    client.datasets.delete('my-dataset')

.. autofunction:: structifyai.operations.DatasetOperations.create
    :no-index:
.. autofunction:: structifyai.operations.DatasetOperations.delete
    :no-index:
.. autofunction:: structifyai.operations.DatasetOperations.info
    :no-index:
.. autofunction:: structifyai.operations.DatasetOperations.list
    :no-index:
.. autofunction:: structifyai.operations.DatasetOperations.query
    :no-index:
