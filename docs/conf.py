import python_docs_theme

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
master_doc = "index"
project = "bakabaka"
year = "2024"
author = "Nic Lu"
copyright = f"{year}, {author}"
version = release = "0.0.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/nic/bakabaka/issues/%s", "#"),
    "pr": ("https://github.com/nic/bakabaka/pull/%s", "PR #"),
}
html_theme = "python_docs_theme"
html_theme_path = [python_docs_theme.get_html_theme_path()]
html_theme_options = {
    "githuburl": "https://github.com/nic/bakabaka/",
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html", "sourcelink.html"],
}
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
