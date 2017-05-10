#-*- coding:utf-8 -*-
___author___ = '12bme'

import scrapy
from tutorial.items import KldpItem

class KldpSpider(scrapy.Spider):#scrapy spider를 상속 받는다.
	name = "kldp"#unique한 이름 지정
	allowed_domains = ["kldp.org"]
	# 스크랩할 url 지정
	start_urls = [
		"https://kldp.org/forum/4",
		"https://kldp.org/forum/5"
	]
	
	# spider 실제 동작 코드
	def parse(self, response):
		'''
		# url 패스의 마지막 글자를 파일이름으로 지정한다.
		filename = response.url.split("/")[-1]
		# 만들어진 파일에 페이지 소스코드를 기록한다.
		with open(filename, "wb") as f:
			f.write(response.body)
		'''
		curPath = response.url.split("/")[-1]
		index = 0
		for sel in response.xpath('//*[@id="forum-topic-'+curPath+'"]/tbody/tr'):
			item = KldpItem() #item에 넣고 싶을때
			index += 1
			item['index'] = index
			item['title'] = sel.xpath('td[2]/div[1]/a/text()').extract()
			item['link'] = sel.xpath('td[2]/div[1]/a/@href').extract() #attribute 값을 가지고 온다
			item['desc'] = sel.xpath('td[2]/div[2]/span/span/text()').extract()
			#print '*'*30
			#print title, link, desc
			yield item 
			'''
			yield는 일종의 generator 개념이라고 생각하면 된다. item이 생성될때마다 리스트형태로 쌓임.
			쌓인 데이터를 어떻게 처리할 것인가에 대한 문제는 pipe라인이나 다른부분에서 처리하면 됨.
			아무튼 yield는 스택형태로 쌓인다.
			'''
