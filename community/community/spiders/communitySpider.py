# -*- coding: utf-8 -*-
__author__='12bme'

import scrapy,re

from community.items import CommunityItem
from datetime import datetime

class CommunitySpider(scrapy.Spider):
	name = "communityCrawler"
	# 크롤링할 사이트의 주소
	# start_urls = []
	
	# 어차피 크롤링은 주기적으로 이루어지는 거니까 주기 고민해서 최신 어디까지 가저올건지 고민.
	def start_requests(self):
		for i in range(1, 2, 1):
			yield scrapy.Request("http://www.clien.net/cs2/bbs/board.php?bo_table=park&page=%d" % i, self.parse_clien) #두번째 변수는 파서
			yield scrapy.Request("http://www.bobaedream.co.kr/list?code=freeb&page=%d" % i, self.parse_bobae)

	def parse_clien(self, response):
		index = 0
		for sel in response.xpath('//html/body/div[2]/div/div[1]/div[5]/div/div'):
			item = CommunityItem()
			
			item['source'] = '클리앙'
			item['category'] = 'free'
			title = sel.xpath('div/div[@class="list-title"]/a[@class="list-subject"]/text()').extract()[0].strip()
			item['title'] = title.encode('utf-8')
			#item['title'] = sel.xpath('td[@class="post_subject"]/a/text()').extract_first()
			item['url'] = 'http://www.clien.net' + sel.xpath('div/div[@class="list-title"]/a[@class="list-subject"]/@href').extract()[0]
			
			#날짜 들고오기
			dateTmp = datetime.strptime(sel.xpath('div/div[@class="list-time"]/span/span[@class="timestamp"]/text()').extract()[0], "%Y-%m-%d %H:%M:%S")
			item['date'] = dateTmp.strftime("%Y-%m-%d %H:%M:%S")
			
			#조회수 들고오기
			hits = sel.xpath('div/div[2]/span/text()').extract()[0].strip()
			item['hits'] = hits
			#item['hits'] = int(td[4].xpath('text()').extract()[0])
			
			index = index + 1			

			print '='*50
			print item['title']
			print "클리앙 " + str(index) + "번째 글 크롤링 완료"
			#print str(unicode('한글','euc-kr').encode('euc-kr'))
				
			yield item
	
	def parse_bobae(self, response):
		index = 0
		for sel in response.xpath('//tbody/tr[@itemtype="http://schema.org/Article"]'):
			item = CommunityItem()
			
			date_now = datetime.now()

			date_str_tmp = sel.xpath('td[@class="date"]/text()').extract()[0]
			prog = re.compile('[0-9]{2}:[0-9]{2}')
			if prog.match(date_str_tmp):
				date_str = date_now.strftime('%y/%m/%d') + ' ' + date_str_tmp + ':00'
			else:
				date_str = date_now.strftime('%y/') + date_str_tmp + ' ' + '00:00:00'

			dateTmp = datetime.strptime(date_str, "%y/%m/%d %H:%M:%S")
			
			item['source'] = '보배드림'
			item['category'] = 'free'
			title = sel.xpath('td[@class="pl14"]/a/text()').extract()[0]
			item['title'] = title.encode('utf-8')
			item['url'] = "http://www.bobaedream.co.kr" + sel.xpath('td[@class="pl14"]/a/@href').extract()[0]
			item['date'] = dateTmp.strftime("%Y-%m-%d %H:%M:%S")
			item['hits'] = int(sel.xpath('td[@class="count"]/text()').extract()[0])

			index += 1
			print '-'*50
			print item['title']
			print '보배드림' + str(index) + "번째 글 크롤링 완료"

			yield item
