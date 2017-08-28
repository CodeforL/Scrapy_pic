# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NidongdeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_id = scrapy.Field()
    name = scrapy.Field()
    pic_url = scrapy.Field()
