# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


import unittest

from structifyai.api.server_api import ServerApi  # noqa: E501


class TestServerApi(unittest.TestCase):
    """ServerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServerApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_version(self) -> None:
        """Test case for version

        Version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
