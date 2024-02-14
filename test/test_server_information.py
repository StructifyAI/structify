# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


import unittest
import datetime

from structifyai.models.server_information import ServerInformation  # noqa: E501

class TestServerInformation(unittest.TestCase):
    """ServerInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServerInformation:
        """Test ServerInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServerInformation`
        """
        model = ServerInformation()  # noqa: E501
        if include_optional:
            return ServerInformation(
                version = ''
            )
        else:
            return ServerInformation(
                version = '',
        )
        """

    def testServerInformation(self):
        """Test ServerInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
