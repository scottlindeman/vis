# -*- coding: utf-8 -*-

# Scrapy settings for aviation project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aviation'

SPIDER_MODULES = ['aviation.spiders']
NEWSPIDER_MODULE = 'aviation.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

DOWNLOAD_DELAY = 0.25  #0.25 seconds

FEED_FORMAT = 'json'

