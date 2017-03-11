#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = 'themes/clean-blog'
HEADER_COVER = 'theme/images/code_big.png'
HEADER_COLOR = 'black'
FACEBOOK_USER = 'Codepodcast'
# SOUNDCLOUD_USER = 'C'
ABOUT_IMAGE = 'theme/css/images/logo.png'
ABOUT_TEXT = 'Code is about concepts behind programming languages, frameworks and libraries. Same beautiful patterns that are present in completely different environments. Occasionally we will invite clever programmers to talk about their favourite techniques. Code is hosted by Andrey Salomatin. '
TWITTER_USER = 'podcastcode'
COPYRIGHT = 'Codepodcast.com'
AUTHOR = 'Michael Beschastnov & Andrey Salomatin'
SITENAME = 'Code Podcast'
SITEURL = 'http://localhost:5000'
DISQUS_SITENAME = 'codepodcast'
ADDTHIS_PUBID = 'ra-55453e963e3042e8'
GOOGLE_ANALYTICS = 'UA-73380046-1'
PATH = 'content'
FB_COMMENTS = 'True'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://codepodcast.com'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
FEED_RSS = 'feeds/all.rss.xml'
TRANSLATION_FEED_ATOM = None
wAUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = 'rss/all'

# Blogroll
# LINKS = (('iTunes', 'https://t.co/LdUNGYyaYU'),
#        ('SoundCloud', 'https://t.co/BID46m8PBT'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/podcastcode'),
                              ('github', 'https://github.com/myprofile'),
                              ('comments-o', 'https://discuss.codepodcast.com/'),
                              ('facebook','https://facebook.com/Codepodcast'),
                              ('envelope','mailto:michael@codepodcast.com'),
                              ('rss','http://codepodcast.com/feeds/all.atom.xml'))
SOCIAL_HEAD = (('soundcloud', 'soundcloud.com/podcastcode'),
                              ('apple','https://geo.itunes.apple.com/us/podcast/code-podcast/id1078095408?mt=2'),
                              ('podcast','http://feeds.soundcloud.com/users/soundcloud:users:201515747/sounds.rss'))
MENUITEMS = (('Episodes','http://codepodcast.net/category/episodes'),
                              ('Blog','http://codepodcast.com/category/blog'),
                              ('Announcements','http://codepodcast.com/category/announcements'))
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = [
            'images',
            'extra/robots.txt',
            'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
            'extra/robots.txt': {'path': 'robots.txt'},
            'extra/favicon.ico': {'path': 'favicon.ico'}
}
