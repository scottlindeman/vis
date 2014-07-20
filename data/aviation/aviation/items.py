# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AviationItem(scrapy.Item):
    date = scrapy.Field()
    time = scrapy.Field()
    operator = scrapy.Field()
    flight_number = scrapy.Field()
    fatalities = scrapy.Field()
    departure = scrapy.Field()
    destination = scrapy.Field()
    crash = scrapy.Field()
