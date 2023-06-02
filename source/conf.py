# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'design_nest'
copyright = '2023, JM AF'
author = 'JM AF'

# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx_design',
        'hoverxref.extension',
        'sphinxcontrib.mermaid',
        "sphinx_carousel.carousel",
        'sphinx_copybutton'
]


hoverxref_auto_ref = True
hoverxref_role_types = {
    "hoverxref": "modal",
    "ref": "tooltip"
}

carousel_show_captions_below = True
carousel_show_controls = True
#'confval': 'tooltip',  # for custom object
#'mod': 'tooltip',  # for Python Sphinx Domain
#'class': 'tooltip',  # for Python Sphinx Domain
mermaid_output_format = "raw"
mermaid_version = "9.4.0"
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

html_theme_options = {
    # Set the name of the project to appear in the navigation.
    # Set you GA account ID to enable tracking
    # 'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://nest-simulator.readthedocs.io/en/latest/',
    'html_minify': False,
    'html_prettify': False,
    'css_minify': True,
    # Set the color and the accent color
    'color_primary': 'orange',
    'color_accent': 'white',
    'theme_color': 'ff6633',
    'master_doc': True,
    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/nest/nest-simulator/',
    'repo_name': 'NEST Simulator',
    # "nav_links": [
    #     {"href": "index", "internal": True, "title": "NEST docs home"}
    #     ],
    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    #'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
    }

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
    'css/popup.css',
    'css/image-map.css',
    'css/page-popup.css',
    'css/overlay.css'
]
html_js_files = [
    'js/custom.js',
    'js/image-map.js',
    #'js/mermaid.js'
    ]
