import os
import sys

# Minimal required Sphinx settings
project = 'hachoir3'
copyright = '2025'
author = 'Project Contributors'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme setting (will be overwritten but required by Sphinx)
html_theme = 'alabaster'