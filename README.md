[![CC BY 4.0][cc-by-shield]][cc-by]  
This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].  

[cc-by]: http://creativecommons.org/licenses/by/4.0/  
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg  

## Contents

1. [Workshop Materials Template](#workshop-materials-template)
2. [Folder Structure](#folder-structure)
3. [Instructions](#instructions)
   1. [Install dependencies](#1-install-dependencies)
   2. [Create a new repository and clone this one](#2-create-a-new-repository-and-clone-this-one)
   3. [Customize the template](#3-customize-the-template)
   4. [Add your content](#4-add-your-content)
   5. [Build the documentation](#5-build-the-documentation)
   6. [Publish the documentation](#6-publish-the-documentation)
   7. [Enable GitHub Pages](#7-enable-github-pages)
4. [Github workflows](#8-github-workflows)
5. [Common warnings and errors](#9-common-warnings-and-errors)


## Workshop Materials Template <a name="workshop-materials-template"></a>

This repository provides a template to host workshop materials using Sphinx to generate HTML documentation from reStructuredText (reST) files. You can use it to organize your workshop presentations, exercises, and materials in a structured and versioned manner.

## Folder Structure <a name="folder-structure"></a>

The repository uses the following structure for organizing multiple workshop versions, each with its own content and slides:
    
```plaintext
workshop-name/
├── docs/
│   ├── build/                          # Contains the generated HTML output
│   ├── source/
│   │   ├── _static/                    # Global static files
│   │       ├── iac-hms-logo-light.png
│   │       ├── iac-hms-logo-dark.png
│   │       └── ...
│   │   ├── _templates/                 # Global templates
│   │   ├── versions/                   # Folder containing versions
│   │       ├── 2024_01_30/             # Version-specific folder
│   │           ├── _static/            # Version-specific static files e.g. PDF slides
│   │               ├── 01_slide.pdf
│   │               └── ...
│   │           ├── 01_slide.rst        # Version-specific content (reST files or Markdown)
│   │           ├── Makefile            # Version-specific Makefile
│   │           └── ...
│   │       ├── 2024_02_15/             # Another version-specific folder
│   │           ├── _static/
│   │               ├── 01_slide.pdf
│   │               └── ...
│   │           ├── 01_slide.rst
│   │           ├── Makefile
│   │           └── ...
│   │   ├── conf.py                     # Single global configuration for all versions
│   ├── build_versions.sh               # Bash script to build all versions
└── ...
```

Each folder in `versions/` corresponds to a specific workshop version, with its own set of slides and content.

## Instructions <a name="instructions"></a>

### 1. Install dependencies <a name="1-install-dependencies"></a>

To install the necessary Python dependencies, run:

```bash
conda create -n fiji-workshop python=3.11
conda activate fiji-workshop
pip install -U sphinx pydata_sphinx_theme sphinx_copybutton
```

### 2. Create a new repository and clone this one <a name="2-create-a-new-repository-and-clone-this-one"></a>

First, create a new repository on the IAC-HMS github to host your workshop materials. Then, download the content of this repository as ZIP, or fetch the template using git:

```bash
git remote add source https://github.com/HMS-IAC/workshop-template.git
git fetch source
git reset --hard source/main  # start exactly from the main branch
git remote remove source  # remove source remote
git push origin main  # push the template content to your new repository; only force the push for the first time
```

### 3. Customize the template <a name="3-customize-the-template"></a>

1. Update each `conf.py` file in the `source/versions` folder with the name of your workshop and your name.

```python
# =============================================================================
#                           Customizable Information
# =============================================================================

# -- Project Information -----------------------------------------------------
project = 'workshop-template'  # Change this to the name of your project
author = 'Antoine A. Ruzette, ... '  # Set the author's name
html_title = 'Workshop Template'  # The title of the website

# =============================================================================
#                    Configuration Settings - Do Not Change
# =============================================================================

...

```

### 4. Add your content <a name="4-add-your-content"></a>

1. Add your slides as PDF files in the `_static` folder of each version.
2. Add your content as reStructuredText (reST) files in the `source/versions` folder of each version.

### 5. Build the documentation <a name="5-build-the-documentation"></a>

This bash script will build the documentation for each version in the `source/versions` folder, as well as creating a entry `index.html` file to redirect to the latest version of the workshop i.e. the most recent one. In the background, it runs the `make html` command independently for each version, and saves the produced html files in `docs/build/`.

It's good practice to start from a clean `build` folder. Note that the `docs` folder also contains a general purpose Makefile to clean up `build`. To do so, run:

```bash
cd docs
make clean
cd ..
```

Then, run the `build_versions.sh` bash script to build the documentation:

```bash
sh docs/build_versions.sh
```

### 6. Publish the documentation <a name="6-publish-the-documentation"></a>

Save in a temporary folder the content of the `docs/build` folder. Then, manually add – or override the existing content – the content of the `docs/build` folder to the root of the `gh-pages` branch of your repository. Make sure your `gh-pages` branch contains a `.nojekyll` file to prevent GitHub from ignoring the `_static` folder.

```bash
git checkout -b gh-pages
touch .nojekyll
git add .
git commit -m "Update workshop materials"
git push origin gh-pages
```

### 7. Enable GitHub Pages <a name="7-enable-github-pages"></a>

Go to the settings of your repository, and under the GitHub Pages section, select the `gh-pages` branch as the source for your GitHub Pages.

## Automating build/publish to gh-pages with workflows <a name="8-github-workflows"></a>

Everything from [build](#5-build-the-documentation) to [publish](#7-enable-github-pages) can be automated using GitHub workflows. The repository contains a `.github/workflows` folder with a workflow that builds the documentation and publishes it to the `gh-pages` branch. The workflow is triggered on push events to the main branch, only if changes to the `docs` folder is detected.

## Common warnings and errors <a name="9-common-warnings-and-errors"></a>

- **`make: sphinx-build: Command not found`**: Make sure you have installed the necessary dependencies.
- **`WARNING: html_static_path entry '_static' does not exist`**: It's alright. The `_static` folder is version-specific and will be created when you add your slides.
- **`WARNING: document isn't included in any toctree`**: This warning is displayed when a reST file is not included in the `index.rst` file. You can safely ignore it if you don't want to include the file in the table of contents.
- **`WARNING: toctree contains reference to nonexisting document`**: This warning is displayed when a file is included in the `index.rst` file but does not exist. Make sure the file is correctly named and located in the right folder.
- **`WARNING: unsupported theme option 'theme_switcher' given`**: This warning is displayed when the `theme_switcher` option is not supported by the theme. It will still display You can safely ignore it.
- **`I can't deploy from GitHub Pages, or files are not displayed with the chosen template`**: Make sure you have created a .nojekyll file in the root of your `gh-pages` branch.
