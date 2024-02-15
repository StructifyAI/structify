# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys

sys.path.insert(0, "/home/dev/src/prospero/client/structify/")

project = "Structify"
copyright = "2024, Alex Reichenbach"
author = "Alex Reichenbach"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "autoapi.extension",
    # "sphinx.ext.autosectionlabel",
    # "sphinxcontrib.redoc",
    # "sphinx.ext.napoleon",
    # "sphinx.ext.autosummary",
]

templates_path = ["/docs/_templates"]
exclude_patterns = []
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
extensions += ["sphinxawesome_theme.highlighting"]
html_title = "Structify"
autoapi_dirs = ["../../../"]
html_baseurl = "/docs/"
html_static_path = ["_static/"]
html_logo = "_static/logo.jpeg"
html_favicon = "_static/favicon.ico"

html_js_files = ["/docs"]
