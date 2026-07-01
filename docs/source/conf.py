# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'GCAM-Europe'
copyright = '2026, Basque Center For Climate Change'
author = 'Basque Center For Climate Change'

release = '1.0'
version = '8.7.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_logo = "_static/logo-diamond.png"

html_theme_options = {
    "logo_only": False,
}

html_css_files = [
    "custom.css"
]
html_show_sourcelink = False

html_js_files = [
    'js/theme.js'
]
