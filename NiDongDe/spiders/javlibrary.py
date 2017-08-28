# -*- coding: utf-8 -*-
import scrapy
from NiDongDe.items import NidongdeItem


class JavlibrarySpider(scrapy.Spider):
    name = 'javlibrary'
    allowed_domains = ['ja14b.com']
    start_urls = ['http://www.ja14b.com/cn/genres.php']
    count = 0
    def parse(self, response):
        genres = {}
        lis = response.xpath('//div[@class="genreitem"]/a')
        for href in lis:
            pic_type = href.xpath('./text()').extract_first()
            
            type_url = 'http://www.ja14b.com/cn/' + href.xpath('./@href').extract_first().replace('?','?&mode=2&')
            genres[pic_type] = type_url

        # for i in genres.values():
            # self.logger.info(i)
            
        # for i in genres.keys():
            # yield scrapy.Request(url = genres[i],callback = self.parse_page)
            
        yield scrapy.Request(url = genres['巨乳'],callback = self.parse_page)

    def parse_page(self,response):
        lis = response.xpath('//div[@class="videos"]/div')
            
        for i in lis:
            item = NidongdeItem()
            item['name_id']=i.xpath('./a/div[@class="id"]/text()').extract_first()
            item['name'] = i.xpath('./a/div[@class="title"]/text()').extract_first()
            item['pic_url'] = ['https:'+i.xpath('./a/img/@src').extract_first().replace('ps.jpg','pl.jpg')]
            yield item
        
        page_next = response.xpath('//a[@class="page next"]')
        if page_next:
            next_url = 'http://www.ja14b.com'+page_next[0].xpath('./@href').extract_first()
            if self.count <30:
                self.count += 1
                yield scrapy.Request(url = next_url,callback = self.parse_page)
            else:
                self.logger.info('chao guo 30 le %s'%response.url)
        else :
            self.logger.info('in the last page%s'%response.url)
                
            
