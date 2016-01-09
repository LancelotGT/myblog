#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ning Wang'
SITENAME = u"Ning Wang"
SITEURL = 'http://localhost:8000'
SITESUBTITLE = '\"A programmer and his cat\"'
THEME = "plumage"

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

LOCALE = 'C'
MD_EXTENSIONS = [
        'codehilite',
        'extra',
        'mdx_video',
        'mdx_titlecase',
]
TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
FILENAME_METADATA = '(?P<slug>.*)'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_PATHS = ['posts']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'search']

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

FEED_RSS = 'feed/index.html'
FEED_ATOM = 'feed/atom/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['posts']
MENUITEMS = [('posts', '/'), ('cv', '/misc/resume.pdf'), ('categories', '/categories.html'), ('archives', '/archives.html')]
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

STATIC_PATHS = ['misc', 'img', 'extra/CNAME']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    # Core plugins
    'related_posts',
    # 'thumbnailer',
    'tipue_search',
    'neighbors',
    'sitemap',
]

TIPUE_SEARCH = True

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5,
            },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly',
            }
}

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
SOCIAL_WIDGET_NAME = "Contact"
SOCIAL = (
            ('@kdeldycke', 'http://twitter.com/kdeldycke'),
)

LINKS_WIDGET_NAME = "Professional profiles"
LINKS = (
        ('Careers 2.0', 'http://careers.stackoverflow.com/kdeldycke'),
        ('LinkedIn', 'http://linkedin.com/in/kevindeldycke/en'),
)

COPYRIGHT = """Unless contrary mentioned, the licensing terms below applies:
<br/>
Code and software released under <a
href='http://www.fsf.org/licensing/licenses/gpl.html'>GNU/GPL licence v2.0</a>;
<br/>
Other content published under <a
href='http://creativecommons.org/licenses/by-sa/3.0/'>Creative Commons
Attribution-Share Alike 3.0 license</a>."""

DISQUS_SITENAME = 'wangnin'

# GOOGLE_ANALYTICS = 'UA-657524-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
