# -*- coding: utf-8 -*-

from scrapy import cmdline
from tutorial import items

cmdline.execute("scrapy crawl douban -o items.json -t json".split())
# cmdline.execute("scrapy crawl douban -o items.csv -t csv".split())