# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Manim Playground'
copyright = '2024, Dibyendu Das'
author = 'Dibyendu Das'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.duration',
  'sphinxcontrib.video',
  'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = 'Examples'
html_static_path = ['_static']

# These paths are either relative to html_static_path or fully qualified paths (eg. https://...)
html_css_files = [
  'css/custom.css'
]

html_js_files = [
  'js/manim-binder.min.js'
]
