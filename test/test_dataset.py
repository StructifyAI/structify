# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


import unittest
import datetime

from structifyai.models.dataset import Dataset  # noqa: E501

class TestDataset(unittest.TestCase):
    """Dataset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Dataset:
        """Test Dataset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dataset`
        """
        model = Dataset()  # noqa: E501
        if include_optional:
            return Dataset(
                description = '',
                name = '',
                schemas = [
                    ''
                    ]
            )
        else:
            return Dataset(
                description = '',
                name = '',
                schemas = [
                    ''
                    ],
        )
        """

    def testDataset(self):
        """Test Dataset"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
