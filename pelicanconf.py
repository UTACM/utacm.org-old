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

# Blogroll
LINKS =  (
        ('UT Computer Science', 'http://www.cs.utexas.edu/'),
        ('Women in CS', 'http://www.cs.utexas.edu/~wics/'),
        ('TSSA', 'http://www.turingscholars.org/'),
        ('ELA', 'http://www.cs.utexas.edu/users/ela/'),
        ('UT Programming Club', 'http://userweb.cs.utexas.edu/users/utpc/'),
        )

# Social widget
SOCIAL = (
        ('Facebook Group', 'https://www.facebook.com/groups/utexas.acm/'),
        ('Events Calendar', 'https://www.google.com/calendar/render?cid=2v4vtrfjc0k2dc3s935gulfr70%40group.calendar.google.com'),
        )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'pdfs']
THEME = 'themes/utacm'
