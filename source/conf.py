# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'InFoDocs'
copyright = 'https://creativecommons.org/licenses/by-sa/4.0/'
author = 'Luis Torres'
release = '0.1'
# The master toctree document.
master_doc = 'index'
html_theme = "sphinx_book_theme"
html_title = "Anotaciones de Informática"
#EPUB
epub_cover = ('_static/portada.png', '')
epub_title = 'Anotaciones de Informática'
epub_author = 'Luis Torres'
epub_publisher = 'Arc Co'
epub_identifier = 'https://github.com/brotherpy/informatica'
epub_language = 'es'
epub_rights = 'cc-by-sa-4.0'

epub_metadata = {
    'dc:creator': 'Luis Torres',
    'dc:publisher': 'Arc Co',
    'dc:rights': 'Licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional',
    'dc:identifier': 'https://github.com/brotherpy/informatica',
    'dc:language': 'es',
}


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser",]
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
