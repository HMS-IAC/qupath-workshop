# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'QuPath Workshop at Harvard Medical School'
copyright = '2024, Antoine A. Ruzette, Simon F. Nørrelykke'
author = 'Antoine A. Ruzette, Simon F. Nørrelykke'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_multiversion",  # For versioning
]

templates_path = ['_templates']  # Make sure the templates directory is included
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = 'pydata_sphinx_theme'

# PyData theme options
html_theme_options = {
    'logo': {
        'text': 'QuPath Workshop',  # Use text if no image logo is available
    },
    'navbar_end': ['navbar-icon-links'],  # Keep this simple since we use the custom version list
    'navbar_persistent': ['search-field'],  # Keep the search field persistent
}

# Sidebar settings for navigation and custom versioning
html_sidebars = {
    "**": ["sidebar-nav-bs", "search-field", "versions.html"],  # Include the custom version list
}

html_static_path = ['_static']
html_logo = "_static/iac-hms-logo.png"
html_title = 'QuPath Workshop at Harvard Medical School'

# -- Options for sphinx-multiversion -----------------------------------------
smv_branch_whitelist = r'^\d{4}_\d{2}_\d{2}$'  # Match branches with date format
smv_branch_exclude = r'^main$'  # Exclude the 'main' branch
smv_tag_whitelist = r'^$'  # Exclude all tags

# Set the HTML base URL for correct linking
html_baseurl = 'https://hms-iac.github.io/qupath-workshop/'
