# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news.items import NewsItem

class ArtikelelektronikSpider(CrawlSpider):
    name = 'artikelelektronik'
    allowed_domains = ['www.liputan6.com']
    start_urls = ['https://www.liputan6.com/tag/ihsg']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('#next.simple-pagination__next-link',)),
             callback="parse_page",
             follow=True),)
             
    def parse_page(self, response):
        print('Processing..' + response.url)
        item_links = response.css('h4 > a::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detil_page)

    def parse_detil_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        article = ' '.join(response.css('.article-content-body__item-content > p::text').extract())
       
        item = NewsItem()
        item['title'] = title
        item['article'] = article
        item['url'] = response.url
        yield item