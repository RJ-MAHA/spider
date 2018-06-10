# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZgcpwswItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    docid = scrapy.Field()
    title = scrapy.Field()
    pubdate = scrapy.Field()
    html = scrapy.Field()
    court = scrapy.Field()
    caseType = scrapy.Field()
    reason = scrapy.Field()
    trialRound = scrapy.Field()
    trialDate = scrapy.Field()
    appellor = scrapy.Field()
    searchKey = scrapy.Field()
    pass
