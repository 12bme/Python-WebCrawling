# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# exception을 통해 필터링 파이프라인 등록해야 비로소 동작함
from scrapy.exceptions import DropItem

class CommunityPipeline(object):
	
	words_to_filter = [u'19금', u'문재인']	

	# item에 관한 필터링 처리
    	def process_item(self, item, spider):
		for word in self.words_to_filter:
			if word in unicode(item['title']):
				print "!!!!! 문재인 exception"
				raise DropItem("Contains forbidden word: %s" % word)
			else:
				return item
