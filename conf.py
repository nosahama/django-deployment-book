# -*- coding: utf-8 -*-
#
# Deploying Django on a single Debian or Ubuntu server documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 10 16:14:04 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.ifconfig',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Deploying Django on a single Debian or Ubuntu server'
copyright = u'2016, Antonis Christofides'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0'
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Deploying Django on a single Debian or Ubuntu server"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = ''

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'DeployingDjangoonasingleDebianorUbuntuserverdoc'

# Number figures
numfig = True


# -- Options for LaTeX output ---------------------------------------------

import textwrap

latex_elements = {
    # See http://stackoverflow.com/questions/3882770/. We keep the releasename
    # empty instead of its default, "Release", to avoid the word "Release" from
    # appearing in the cover page.
    'releasename': '',

    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a5paper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # In order to include some information in the inner cover page, we manually
    # insert a table of contents in main_toctree.rst, so we tell it to not
    # generate the one it would normally generate.
    'tableofcontents': '',

    # Custom cover
    'maketitle': r'\includepdf{../../cover.pdf}',

    # Minor changes in Latex formatting
    'preamble': textwrap.dedent(r'''
        % Margins 2cm, useful for a5paper, must be changed in other sizes
        \usepackage{anysize}
        \marginsize{2cm}{2cm}{2cm}{2cm}

        % Use pdfpages for front cover
        \usepackage{pdfpages}

        % Use txtt fontface for verbatim, and make it slightly smaller if inline
        \renewcommand{\code}[1]{\texttt{\small{#1}}}
        \renewcommand{\ttdefault}{txtt}

        % Don't give floats their own page, unless they're more than 80% of
        % the page.
        \renewcommand{\floatpagefraction}{.8}

        % See http://stackoverflow.com/questions/3882770/. We've copied the following
        % from sphinx.sty, and changed it so that it does not show the release name in
        % the page header. (Not sure it's needed though, maybe just keeping the
        % release name empty can work, and maybe it depends on Sphinx version.)

        \makeatletter

        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
            \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
            \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
            \fancyhead[LE,RO]{{\py@HeaderFamily \@title}}
            \renewcommand{\headrulewidth}{0.4pt}
            \renewcommand{\footrulewidth}{0.4pt}
            % define chaptermark with \@chappos when \@chappos is available for Japanese
            \ifx\@chappos\undefined\else
            \def\chaptermark##1{\markboth{\@chapapp\space\thechapter\space\@chappos\space ##1}{}}
            \fi
        }

        \makeatother
        '''),
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'DeployingDjangoonasingleDebianorUbuntuserver.tex', u'Deploying Django on a single Debian or Ubuntu server',
   u'Antonis Christofides', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'deployingdjangoonasingledebianorubuntuserver', u'Deploying Django on a single Debian or Ubuntu server',
     [u'Antonis Christofides'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'DeployingDjangoonasingleDebianorUbuntuserver', u'Deploying Django on a single Debian or Ubuntu server',
   u'Antonis Christofides', 'DeployingDjangoonasingleDebianorUbuntuserver', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Deploying Django on a single Debian or Ubuntu server'
epub_author = u'Antonis Christofides'
epub_publisher = u'Antonis Christofides'
epub_copyright = u'2016, Antonis Christofides'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'Deploying Django on a single Debian or Ubuntu server'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
epub_cover = ('_static/cover.png', 'epub-cover.html')

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True
