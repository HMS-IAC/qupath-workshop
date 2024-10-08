import os

# =============================================================================
#                           Customizable Information
# =============================================================================

# -- Project Information -----------------------------------------------------
project = 'qupath-workshop'  # Change this to the name of your project
author = 'Antoine A. Ruzette, Simon F. Nørrelykke'  # Set the author's name
html_title = 'QuPath workshop'  # The title of the website

# =============================================================================
#                    Configuration Settings - Do Not Change
# =============================================================================

# -- Repository and URL Configuration ----------------------------------------
# no need to change if your repository is hosted on the IAC-HMS GitHub
iac_url = "https://iac.hms.harvard.edu/"  # Institution website URL
github_url = "https://github.com/HMS-IAC"  # GitHub organization URL

# Copyright information
copyright = '(2024) Antoine A. Ruzette, Simon F. Nørrelykke'

# -- General Sphinx Configuration --------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# Exclude patterns (add any files or directories you want to ignore)
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML Output Configuration -----------------------------------------------
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    'logo': {
        'text': html_title,
        'image_light': os.path.join('_static', 'iac-hms-logo-light.png'),
        'image_dark': os.path.join('_static', 'iac-hms-logo-dark.png'),
    },

    'navbar_end': ['navbar-icon-links', 'theme-switcher'],
    "navbar_persistent": [],
    "navbar_center": [],
    'icon_links': [
        {
            "name": "IAC",
            "url": iac_url,
            "icon": "fa-solid fa-globe",
        },
        {
            "name": "GitHub",
            "url": github_url,
            "icon": "fa-brands fa-github",
        }
    ],
}


# Templates path (global)
templates_path = ['_templates']

# Sidebar configuration
html_sidebars = {
    "**": ["sidebar_versions.html", "globaltoc"],
}

# -- Static Files Configuration ----------------------------------------------
html_static_path = [os.path.abspath('_static')]

# -- Version Handling (Optional) ---------------------------------------------
# Detect the current version and manage versions folder
current_version = os.getenv('CURRENT_VERSION', None)
versions_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../versions'))

if current_version:
    version_static_path = os.path.join('versions', current_version, '_static')
    if os.path.isdir(version_static_path):
        html_static_path.insert(0, version_static_path)
        print(f"Added {version_static_path} to html_static_path")

# -- Automatically Detect and Display Versions ------------------------------
versions_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'versions'))
versions = [d for d in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, d))]

html_context = {
    'versions': [{'name': v, 'url': f'/{project}/versions/{v}/index.html'} for v in versions],
}
