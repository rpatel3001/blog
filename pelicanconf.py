#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Rajan Patel'
SITETITLE = AUTHOR
SITESUBTITLE = 'Computer Engineering Student'
SITENAME = "%s's Blog" % AUTHOR
MAINURL = 'https://rajanpatel.net'
SITEURL = MAINURL
SITEDESCRIPTION ="%s's Blog" % AUTHOR
SITELOGO = SITEURL + '/images/logo.png'
FAVICON = SITEURL + '/images/logo.png'

ROBOTS = 'all'

SHOW_POST_AUTHOR = True

COPYRIGHT_YEAR = 2019

DEFAULT_DATE_FORMAT = '%a %B %d %Y'

DISQUS_SITENAME = 'rajanpatel'

MAIN_MENU = True

PATH = 'content'
STATIC_PATHS = ['images', 'css']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

PYGMENTS_STYLE = 'manni'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_METADATA = {
    'status': 'draft',
}

# Blogroll
LINKS = (('RU Interested', '%s/ru-interested' % MAINURL),
         ('ESP32 Reporting', '%s/api/esp_view' % MAINURL),)

# Social widget
SOCIAL = (('github', 'https://github.com/rpatel3001'),
          ('facebook', 'https://www.facebook.com/rpatel3001'),
	  ('twitter', 'https://twitter.com/rpatel3001'),
	  ('linkedin', 'https://linkedin.com/in/rkp8966'))
TWITTER_USERNAME = 'rpatel3001'
GITHUB_CORNER_URL = 'https://github.com/rpatel3001'

MENUITEMS = (('Archives', '%s/archives.html' % SITEURL),
             ('Categories', '%s/categories.html' % SITEURL),
             ('Tags', '%s/tags.html' % SITEURL),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISABLE_URL_HASH = True
PORT = 8001
TYPOGRIFY = True
GOOGLE_ANALYTICS = 'UA-42154912-1'
THEME = 'theme/Flex'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search', 'post_stats', 'related_posts', 'representative_image', 'neighbors']
CUSTOM_CSS = 'css/main.css'
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives', 'search'))
#DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'authors', 'archives'))

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-7821329515419218',    # Your AdSense ID
    'page_level_ads': True,          # Allow Page Level Ads (mobile)
    'ads': {
#        'aside': '1234561',          # Side bar banner (all pages)
#        'main_menu': '1234562',      # Banner before main menu (all pages)
#        'index_top': '1234563',      # Banner after main menu (index only)
#        'index_bottom': '1234564',   # Banner before footer (index only)
#        'article_top': '1234565',    # Banner after article title (article only)
#        'article_bottom': '1234566', # Banner after article content (article only)
    }
}
