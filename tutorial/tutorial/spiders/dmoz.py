# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoztools.net']
    start_urls = ['http://www.dmoztools.net/Games/Video_Games/Directory/',
                  'http://www.dmoztools.net/Games/Online/Directories/'
                  ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()[0]
            item['link'] = site.xpath('a/@href').extract()[0]
            item['desc'] = site.xpath('div[@class="site-descr "]/text()').extract()[0].strip()
            items.append(item)
        return items


        # file_name = response.url.split('/')[-2]
        # with open(file_name, 'wb') as f:
        #     f.write(response.body)
