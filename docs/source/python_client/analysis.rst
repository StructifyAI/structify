.. _Analyzing Datasets:

Analyzing Your Datasets
=======================

Overview
--------

Part of the advantages to using Structify as a backend is the automatic powering of advanced analytics on top of your custom datasets. Currently, Structify powers the following:

#. :ref:`Creating Custom Tags for Data <tagging>`
#. :ref:`Sorting Data along Any Axis <sorting>`
#. :ref:`Retreiving the Sources for Your Data <backsourcing>`
#. :ref:`Getting Confidence Scores <confidence>`


.. _tagging:

Tagging
-------
We allow for you to tag data either via LLM generated tags or custom tags. This allows for you to easily filter your data based on the tags you have created.

A common practice is to sort datasets by industry. For example, if you are hiring a GTM specialist, you would want them to have deep knowledge and contacts within your vertical, so tagging your network by industry would allow you to easily filter for the right candidates. You can see a great example of this in `our tutorial <example/example3>`.

.. code-block:: python

    industry_tags = ['healthcare', 'retail', 'finance', 'technology', 'education', 'government', 'non-profit', 'other']
    Structify.analysis.filter(dataset=candidates, tags=industry_tags, tag_description="a list of possible industries that the candidate has experience in")


.. _sorting:

Sorting
-------
We allow for you to sort your data along any axis (subjective or objective). For example, you can sort news about clients along the sentiment to see how sentiment has changed over time, or you could cluster based on topic and sentiment to determine why audiences are reacting the way they are.

.. code-block:: python

    Structify.analysis.sort(dataset=news, axis=['sentiment', 'topic'], sort_description="sorts the news by sentiment in order of positive association with our client George Washington University")

.. _backsourcing:

Backsourcing
------------
This endpoint allows you to retrieve all the sources used to validate and create any given datapoint. This is useful for understanding the provenance of a given datapoint and for understanding the context in which it was created.

To use this endpoint, you would call the following:

.. code-block:: python

    target_datapoint = {
        entity: {
            "name": "George Washington University",
            "table": {
                "name": "professors",
                "columns": ["name", "title", "department", "email", "phone", "office"],
                "rows": [{"name": "John Smith", "title": "Chair Emeritus", "department": "Biology"}]
            }
        }
    }
    Structify.analysis.backsource(dataset=news, target=target_datapoint)

In this example, the API is able to produce the backsourcing for multiple sources that were used to validate the data associated for the professor John Smith at George Washington University.

.. _confidence:

Confidence Scores
-----------------
We allow for you to get confidence scores for any given datapoint. This is useful for understanding the quality of the data, and for understanding how strongly our agents feel about the certainty of a given datapoint.

If we wanted to get the confidence score for John Smith's email address, we would call the following:

.. code-block:: python

    target_datapoint = {
        entity: {
            "name": "George Washington University",
            "table": {
                "name" : "professors",
                "columns" : ["email"],
                "rows" : [{"name": "John Smith", "title": "Chair Emeritus", "department": "Biology"}]
            }
        }
    }
    Structify.analysis.confidence_score(dataset = news, target = target_datapoint)

Now, you have the tools to be able to more deeply understand your datasets and derive insights from them.