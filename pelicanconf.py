#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = 'Rajan Patel'
SITETITLE = AUTHOR
SITESUBTITLE = 'Computer Engineering Student'
SITENAME = '%s\'s Blog' % AUTHOR
MAINURL = 'https://rajanpatel.net'
SITEURL = '%s/blog' % MAINURL
SITEDESCRIPTION ='%s\s Random Crap' % AUTHOR
SITELOGO = SITEURL + '/images/logo.png'
FAVICON = SITEURL + '/images/logo.png'

COPYRIGHT_YEAR = 2019

DEFAULT_DATE_FORMAT = '%a %B %d %Y'

DISQUS_SITENAME = 'rajanpatel'

MAIN_MENU = True

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_METADATA = {
    'status': 'draft',
    'author': 'Rajan Patel'
}

# Blogroll
LINKS = (('RU Interested', '%s/ru-interested' % MAINURL),)

# Social widget
SOCIAL = (('github', 'https://github.com/rpatel3001'),
          ('facebook', 'https://www.facebook.com/rpatel3001'),
	  ('twitter', 'https://twitter.com/rpatel3001'),
	  ('linkedin', 'https://linkedin.com/in/rkp8966'),
	  ('rss', '//rajanpatel.net/blog/%s' % FEED_ALL_ATOM))
TWITTER_USERNAME = 'rpatel3001'

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