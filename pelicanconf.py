#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'William Ting'
SITENAME = u'Association for Computing Machinery'
TAGLINE = u'University of Texas Chapter'
SITEURL = ''

TIMEZONE = 'America/Chicago'

DEFAULT_CATEGORY = u'general'
DEFAULT_LANG = u'en'
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']
THEME = 'themes/utacm'
FILES_TO_COPY = [('images/favicon.ico', 'favicon.ico')]
