# coding: utf-8

# flake8: noqa

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


__version__ = "0.0.2"

# Import our wrapper object
from structifyai.api_client import Client

# import apis into sdk package
from structifyai.api.dataset_api import DatasetApi
from structifyai.api.server_api import ServerApi

# import ApiClient
from structifyai.api_response import ApiResponse
from structifyai.api_client import ApiClient
from structifyai.configuration import Configuration
from structifyai.exceptions import OpenApiException
from structifyai.exceptions import ApiTypeError
from structifyai.exceptions import ApiValueError
from structifyai.exceptions import ApiKeyError
from structifyai.exceptions import ApiAttributeError
from structifyai.exceptions import ApiException

# import models into sdk package
