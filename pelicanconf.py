#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'William Ting'
SITENAME = u'Association for Computing Machinery'
TAGLINE = u'University of Texas Chapter'
SITEURL = ''
RELATIVE_URLS = True

TIMEZONE = 'America/Chicago'

DEFAULT_CATEGORY = u'general'
DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = ['images', 'pdfs']
FILES_TO_COPY = [('images/favicon.ico', 'favicon.ico')]

THEME = 'theme'
MENUITEMS = [('Home', '/')]
