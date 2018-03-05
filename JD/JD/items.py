# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    sku = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    plus_price = scrapy.Field()
    subtitle = scrapy.Field()
    if_ziying = scrapy.Field()
    labels = scrapy.Field()
    sales = scrapy.Field()
    store_name = scrapy.Field()
    cate_ID = scrapy.Field()