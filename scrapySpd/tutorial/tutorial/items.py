# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanItem(scrapy.Item):
    movie_name = Field()  # 电影名字
    movie_desc = Field()  # 描述
    movie_star = Field()  # 评分
    movie_quote = Field()  # 格言
