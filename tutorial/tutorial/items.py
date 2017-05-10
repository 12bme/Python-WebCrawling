# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

'''
파이썬 주석 처리
'''

'''
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
'''
import scrapy

class KldpItem(scrapy.Item):
	index = scrapy.Field()
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()
