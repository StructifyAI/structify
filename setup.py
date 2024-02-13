# coding: utf-8

"""
    Structify

    Unify all your unstructured knowledged into one structured source.

    Version: 0.1.0

    Contact: team@structify.ai
"""


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "structifyai"
VERSION = "0.0.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Structify",
    author="Structify Team",
    author_email="team@structify.ai",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Structify"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Discuss directly with founders for license.",
    long_description_content_type='text/markdown',
    long_description="""\
    Unify all your unstructured knowledged into one structured source.
    """,  # noqa: E501
    package_data={"structifyai": ["py.typed"]},
)
