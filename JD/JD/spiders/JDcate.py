#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem
import logging
from scrapy_redis.spiders import RedisSpider
import time

# class JDcat(scrapy.Spider):
class JDcat(RedisSpider):
    name = "JDcate"
    allowed_domains = ["jd.com"]

    # scrapy-redis
    redis_key = "JDcate:JD_urls"

    def start_requests(self):
        # designed by yourself
        # yield scrapy.Request(url=url, callback=self.parse)
        pass

    def parse(self, response):
        # designed by yourself
        pass






