# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MonsterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title     = scrapy.Field()
    job_city  = scrapy.Field()
    job_state = scrapy.Field()
    company   = scrapy.Field()
    des       = scrapy.Field()
    date      = scrapy.Field() # post date


