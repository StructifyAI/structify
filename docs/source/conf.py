# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys

sys.path.insert(0, "/home/dev/src/prospero/client/structify/")

project = "Structify"
copyright = "2024, Alex Reichenbach & Ronak Gandhi"
author = "Alex Reichenbach & Ronak Gandhi"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinx.ext.autosummary",
    # "sphinx.ext.autosectionlabel",
    # "sphinxcontrib.redoc",
    # "sphinx.ext.napoleon",
]

templates_path = ["/docs/source/_templates"]
exclude_patterns = []
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
extensions += ["sphinxawesome_theme.highlighting", "sphinxcontrib.details.directive"]
html_title = "Structify"
autoapi_dirs = ["../../../"]
html_baseurl = "/docs/"
html_static_path = ["_static/"]
html_logo = "_static/webclip.png"
html_favicon = "_static/favicon.png"

html_js_files = ["/docs"]

"""
# Configuration for the sidebar
html_sidebars = {
    '**': [
        'sidebar.html',  # Main sidebar
        'globaltoc.html',  # Table of contents
        'localtoc.html',   # Subsection TOCs
        'searchbox.html',  # Search box
    ]
}

"""
