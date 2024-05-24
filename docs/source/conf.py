# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'QuPath Workshop at Harvard Medical School'
copyright = '2024, Antoine A. Ruzette, Simon F. Nørrelykke. Licensed under CC-BY 4.0 International.'
author = 'Antoine A. Ruzette, Simon F. Nørrelykke'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]
autodoc_typehints = "both"
napoleon_use_ivar = True

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/iac-hms-logo.png"  # Specify the path to your logo file
html_title = 'QuPath Workshop at Harvard Medical School'