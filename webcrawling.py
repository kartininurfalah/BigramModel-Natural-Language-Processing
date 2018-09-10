# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 08:46:39 2018

@author: kartini
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class WebCrawling(CrawlSpider):
    name = "electronics"
    allowed_domains = ["www.merdeka.com"]
    start_urls = [
        'www.merdeka.com/indeks-berita/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)