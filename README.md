[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

# QuPath workshop at Harvard Medical School
This deck of slides introduces participants to the main ideas of bioimage analysis using the open-source software [QuPath](https://qupath.github.io/). It is designed as a primer on QuPath for biologists who need to analyze images part of their research. These materials were initially designed for a workshop taught in-person at Harvard Medical School - organized by the [Image Analysis Collaboratory](https://iac.hms.harvard.edu/). 

# Update materials with Sphinx

This repository uses Sphinx to generate documentation from reStructuredText (reST) files. Typically, one would simply modify the slides and replace the relevant file in `docs/source`. Then, file paths have to be updated in the documentation as described below. 

## Getting started

To modify the content of this repository, follow these steps:

1. **Clone the repository**: Clone this repository to your local machine using Git.

    ```bash
    git clone https://github.com/HMS-IAC/qupath-workshop.git
    ```

2. **Create an environment**: For example, using conda. 
    ```bash
    conda create -n iac-qupath-workshop python=3.10
    conda activate iac-qupath-workshop
    ```

3. **Install Sphinx**: If you haven't already installed Sphinx, you can do so using pip. `furo` is the Sphinx theme used. 

    ```bash
    pip install sphinx pydata_sphinx_theme sphinx_copybutton sphinx-multiversion
    ```

4. **Navigate to /docs**: Navigate to the directory containing the documentation source files.

    ```bash
    cd docs
    ```

5. **Modify and build for as single version**: Edit the `.rst` files in the source directory to make changes to the documentation content. You can use any text editor to modify these files. Then, build the html files. 

    ```bash
    make clean
    ```

    ```bash
    make html
    ```: 

6. **Build multiple versions with sphinx-multiversion**: The `sphinx-multiversion` extension allows control versions across github branches. The materials for an edition should be contained in its own branch. This extension will build the html files for each branch and version. It is recommended to run this command from the root directory of the `main` branch, and keep a `gh-pages` branch clean for page publication.

    ```bash
    cd docs
    make clean
    cd ..
    sphinx-multiversion docs/source/ docs/build/html 
    ```

8. **HTML files**: After building the documentation, you can view the updated the HTML files located in the `docs/build/html` directory.

9. **Move the content of `docs/build/html` to root directory of gh-pages branch**: use a `tmp` folder, and drog and drop the folders (each folder contains the materials of a version) to the root of the publishing branch. 

10. **Commit and Push Changes**: After verifying that the documentation looks as expected by opening local html file, commit your changes and push them to the repository.

    ```bash
    cd ..
    git add .
    git commit -m "Update documentation"
    git push
    ```

## Additional resources

- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/): Official documentation for Sphinx.
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html): Learn the basics of reStructuredText (reST) markup language.
