#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tiel'
SITENAME = 'Litneria'
SITETITLE = 'Litneria'
SITESUBTITLE = 'Together We Soar'
SITEURL = 'https://litneria.herokuapp.com'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Application','http://tinyurl.com/Litneriapp'), ('Discord','http://tinyurl.com/LitneriaDiscord'))

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

THEME = 'theme/flex/'

USE_LESS = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets','extract_toc','summary','clean_summary','thumbnailer']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
