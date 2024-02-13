# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


import unittest

from structifyai.api.dataset_api import DatasetApi  # noqa: E501


class TestDatasetApi(unittest.TestCase):
    """DatasetApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DatasetApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create a Dataset  # noqa: E501
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Remove a kg from the database  # noqa: E501
        """
        pass

    def test_get(self) -> None:
        """Test case for get

        Remove a kg from the database  # noqa: E501
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List knowledge graph  # noqa: E501
        """
        pass

    def test_query(self) -> None:
        """Test case for query

        Remove a kg from the database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
