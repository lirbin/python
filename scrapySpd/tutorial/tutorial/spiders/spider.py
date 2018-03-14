# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from tutorial.items import DoubanItem
from scrapy.http import Request


class DoubanSpider(scrapy.Spider):
    name = "douban"
    # allowed_domains = ["movie.douban.com"] #这个域，还不知道啥用
    # allowed_domains = ["www.baidu.com/"]
    url = 'https://movie.douban.com/top250/'
    start_urls = [
        "https://movie.douban.com/top250",
        # "https://movie.douban.com/top250/?start=25&filter=",
        # "https://www.baidu.com/",
    ]

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        # body = response.body
        # unicode_body = response.body_as_unicode()
        movies = selector.xpath('//div[@class="info"]')
        for eachMovie in movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()

            fullTitle = ''
            for each in title:
                fullTitle += each
            desc = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''

            # print(fullTitle)
            # print(movie_desc)
            # print(star)
            # print(quote)

            item['movie_name'] = fullTitle
            item['movie_star'] = star
            item['movie_desc'] = ';'.join(desc)
            item['movie_quote'] = quote
            yield item

            nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()

            if nextLink:
                next = nextLink[0]
                print(next)
                yield scrapy.http.Request(self.url+next, callback=self.parse)
