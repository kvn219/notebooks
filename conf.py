#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sphinx_bootstrap_theme

html_logo = "_static/logo.png"

extensions = [
    'nbsphinx',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]


templates_path = ['_templates']
source_suffix = ['.rst', '.ipynb']
master_doc = 'index'

project = 'Notebooks'
copyright = '2018, Kevin Nguyen'
author = 'Kevin Nguyen'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
pygments_style = 'sphinx'
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {
    'navbar_title': "Notebooks",
    'navbar_site_name': "Notebooks",
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'globaltoc_depth': 1,
    'globaltoc_includehidden': "true",
    'navbar_class': "navbar",
    'navbar_fixed_top': "true",
    'source_link_position': "",
    'bootswatch_theme': "paper",
    'bootstrap_version': "3",
}


html_static_path = ['_static']

latex_documents = [
    (master_doc, 'Notebooks.tex', 'Notebooks Documentation',
     'Kevin Nguyen', 'manual'),
]
man_pages = [
    (master_doc, 'notebooks', 'Notebooks Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Notebooks', 'Notebooks Documentation',
     author, 'Notebooks', 'One line description of project.',
     'Miscellaneous'),
]


def setup(app):
    app.add_stylesheet('css/custom.css')
