# Update materials with Sphinx

This repository uses Sphinx to generate documentation from reStructuredText (reST) files. Typically, one would simply modify the slides and replace the relevant file in `docs/source`. Then, file paths have to be updated in the documentation as described below. 

## Getting Started

To modify the content of this repository, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git.

    ```bash
    git clone <repository-url>
    ```

2. **Install Sphinx**: If you haven't already installed Sphinx, you can do so using pip.

    ```bash
    pip install sphinx furo 
    ```

3. **Navigate to the Documentation Directory**: Navigate to the directory containing the documentation source files.

    ```bash
    cd docs
    ```

4. **Modify the Documentation**: Edit the `.rst` files in the source directory to make changes to the documentation content. You can use any text editor to modify these files.

5. **Build the Documentation**: Once you've made your changes, rebuild the documentation using the `make` command.

    ```bash
    make clean
    ```

    ```bash
    make html
    ```

6. **View the Documentation**: After building the documentation, you can view the updated the HTML files located in the `docs/build/html` directory.

7. **Move the content of `docs/build/html` to root directory**: drog and drop the whole folder. 

7. **Commit and Push Changes**: After verifying that the documentation looks as expected, commit your changes and push them to the repository.

    ```bash
    git add .
    git commit -m "Update documentation"
    git push
    ```

## Additional Resources

- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/): Official documentation for Sphinx.
- [reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html): Learn the basics of reStructuredText (reST) markup language.
