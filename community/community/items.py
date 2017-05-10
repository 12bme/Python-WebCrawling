# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CommunityItem(scrapy.Item): # 최초 클래스 생성시 아이템을 입력하여 만들면 됨
	# define the fields for your item here like:
	# name = scrapy.Field()
	source = scrapy.Field()
	category = scrapy.Field() # 어디 게시판에서 가져오는지 표시
	title = scrapy.Field()
	url = scrapy.Field()
	hits = scrapy.Field()
	date = scrapy.Field()
	pass
