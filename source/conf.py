# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'InFoDocs'
copyright = '2024, Luis Torres'
author = 'Luis Torres'
release = '0.1'
# The master toctree document.
master_doc = 'index'
html_theme = "sphinx_book_theme"
html_title = "Anotaciones de Informática"
#EPUB
epub_title = "Anotaciones de Informática"
epub_language = "es"
epub_metadata = {
    'dc:creator': 'Luis Torres',
    'dc:publisher': 'ARC Co',
    'dc:rights': 'Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional',
    'dc:identifier': 'unique-identifier',
    'dc:language': 'es',
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
# Use the MyST parser for Markdown
source_parsers = {
    '.md': ' myst_parser',
}


templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_static_path = ['_static']
