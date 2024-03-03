Notifications
==============
A ton of the power in Structify is the ability to automatically monitor datasets for significant changes whenever a refresh happens. We allow users to create a notification or alert that will be triggered when a certain data point in a dataset gets updated. Users can specify the conditions under which the notification should be triggered, such as when a specific cell, column, or row is updated, or when the value of a data point changes to a specific value.

In order to create a notification, users must specify the following details in a dictionary and pass that as a parameter:

- **name:** (required) The name of the notification
- **target**: (required) The target data point to monitor for updates. This can be specified as a combination of entity name, table name, row name, and column name, or as a specific cell address.
- **destination**: (required) Where the notification will be triggered to. This can be specified as:
    * *webhook*: Users can specify a webhook URL to which the notification payload will be sent.
    * *SMS*: The user must input a valid phone number where the notification will be sent.
    * *email*: The user must input a valid email address
- **condition**: (optional) The condition under which the notification should be triggered. This can be specified as:
    * *value_changed*: Trigger the notification when the value of the target data point changes.
    * *value_equals*: Trigger the notification when the value of the target data point equals a specific value.
    * *value_added*: Trigger the notification when a new row is added to a table or an entity to a dataset.
- **value**: (optional) The specific value to monitor for changes. Required if condition is set to *value_equals*.

.. code-block:: python

    notification_details = {
        "name" : "new_job",
        "target": {
            "entity_name" : "John Kim",
            "table_name": "jobs",
        },
        "destination" : "webhook",
        "condition": "value_added",
    }

    notification = Structify.notification.create(name = "employees", json=notification_details)

This example outlines the creation of a webhook notification that will alert us anytime John Kim starts a new job. Specifically, the notification will be triggered when a new row is added to the jobs table in the John Kim entity.