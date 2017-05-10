# Python-WebCrawling
"파이썬을 이용한 웹 크롤링(Web Crawling) 어플리케이션 만들기" 강좌기반 파이썬 웹크롤러 프로젝트
- - - 
### 백엔드란
사용자의 요청을 받아서, __저장되어 있는 정보를 바탕으로 각 사용자에게 적합한 페이지__ 를 전송.
1. 웹 서버(Apache, IIS, nginx, GWS, etc.) 
   * 사용자의 요청에 맞게 데이터(HTML, image, etc.)를 전송해주는 프로그램
2. 데이터 베이스(MySql, Oracle, MsSql, PostgreSQL, LightSql, MongoDB, etc.)
   * 사용자의 정보를 저장하는 저장소
3. 스크립트 엔진(php, jsp, asp)
   * 웹서버에서 사용자의 요청을 분석해주는 프로그램
4. 웹프레임워크(Django, Ruby onRails, etc)
   * 웹개발을 보다 편리하게 만들어 주는 도구
   * 웹서버, 데이터베이스 등 역할 일부 지원
   * 쿼리작업까지도 웹프레임워크가 진행

__웹서버, 스크립트엔진에 대한 이해 필요__

- - -

### Web-Crawler Overview
WebServer(Apache2) | Database(MySql)
Crawler(Beautiful Soup 4) | Django 1.8 | Python 2.7
OS (Ubuntu 14.04)
Cloud Service (Google Compute Engine)

### Python을 이용한 웹크롤링
* 개발환경구축
* BeautifulSoup 4.x(데이터를 가져오는데 특화된 라이브러리), Scrapy(크롤링에서 강력 / 크롤링전용 라이브러리)
* 사이트 구조 분석 방법
* 특정 사이트 데이터 취득

- - -

## 개발환경
* 운영체제 : Ubuntu 16.04.2
* 언어 : Python 2.7
* 사용 라이브러리 : BeautifulSoup, Scrapy
   * BeautifulSoup보다 Scrapy가 더 강력, 그래서 Scrapy로 진행될 것
* 기타 : virtualenv, virtualenvwrapper, docker
   * 버전 맞춰주는 것도 일이여서 가상환경에 알맞은 패키지 버전 설치하면 깔끔하게 파이썬 쓸수 있음

__크롤링은 주로 링크나 텍스트를 복사__<br/>
__우분투를 쓰는 이유는, 사용자가 많아서 여러가지 반영이 쉽게 됨__

* Beautiful Soup 설치 전 필요한 패키지 있음
  * apt-get install libxml2-dev libxslt-dev python-dev zlib1g-dev
  * apt-get install python-lxml
  * pip install lxml (파이썬 환경에서의 lxml 설치)
* 의존패키지 설치 완료 후, beautifulsoup 설치
  * pip install beautifulsoup4

* Scrapy 설치 전 필요한 패키지 있음
  * apt-get install libffi-dev libssl-dev
* 의존패키지 설치 완료 후, Scrapy 설치

__가상환경은 프로젝트의 충돌을 방지__

- - -

## Beautiful Soup VS Scrapy
* Beautiful Soup
   * html문서에서 원하는 정보를 손쉽게 가져올 수 있는 방법을 제공.
   * 자동으로 인코딩을 유니코드로 변환해서 UTF-8로 출력.
   * lxml, html5lib 파서를 이용함
   * http://www.crummpy.com/software/BeautifulSoup/bs4/doc/

* Scrapy
   * web scraper framework
   * 다양한 selector 지원
   * 파이프 라인(데이터 필터링)
   * 로깅(데이터 잘 들어오는지)
   * 이메일(데이터 들어왔을때 이메일 전송)
   * http://doc.scrapy.org/en/0.24/intro/tutorial.html


* Beautiful Soup은 HTML의 문서를 가져와서 파싱을 해주는 파서의 역할이 강하며,<br/>
  문서를 가져와서 네비게이션하는 기능이나 자동으로 인코딩을 유니코드로 변환해서 UTF-8로 출력.

* Scrapy는 Web에서 데이터를 들고와서 하는 전체적 내용을 프레임워크 형태로 제작한 라이브러리.<br/>
  프레임워크라 다양한 기능지원(파이프라인, 로깅, 이메일)

* Beautiful Soup에도 파이프라인, 로깅, 이메일 기능이 있는데, 직접 구현해야함.


* Beautiful Soup 레퍼런스 일부 발췌
<pre>
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

soup.title
<title>The Dormouse's story</title>

soup.title.name
u`title`

soup.title.string
The Dormouse's story

soup.title.parent.name
u`head`

soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a') : 가장 많이 쓰이는 명령어.
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find(id="link3")
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

soup.find_all(href=re.compile("elsie"), id='link1')
[<a class="sister" href="http://example.com/elsie" id="link1">three</a>]

data_soup.find_all(attrs={"data-foo":"value"})
[<div data-foo="value">foo!</div>]
</pre>

__태그 이름이나 css 속성, 정규식을 통해서도 데이터를 수집하는 것이 가능함.__

__Scrapy의 경우, 데이터를 들고올때 클래스형태로 만들 수 있습니다.__
* items.py 웹환경에서 title, 링크, 글을 쓴 저자를 가져오고자 할때, Item에서의 지정이 가능
* pipelines.py 어떤 Scrapy를 통해 데이터를 들고와서 그 데이터에 대해 후처리를 하고 싶을때, 데이터 필터링이나 데이터베이스에 입력하고 싶을때
* settings.py spider라고 부르는데, spider에 대한 설정들이 들어있음.
* spiders 폴더 안에는 실제 불러오고싶은 내용에 대한 코드가 위치한다.

- - -

__scrapy crawl "스파이더명"__
__스파이더는 여러개 만들어서 동시 실행이 가능.__

__크론탭을 이용해서 크롤링 관련 배치작업 설정할 수 있음.__


- - -

# Scrapy를 이용해서 웹데이터를 크롤링하는 방법
Scrapy에 대한 전반적인 이야기, 사이트에서 실제 데이터를 가져오는 것까지


## 목차
1. 웹 크롤링 이슈
   * 웹데이터 저작권
   * 사이트의 크롤링 정책
2. scrapy 구조
3. scrapy
   * spiders
   * selector
   * pipline
   * logging
4. 웹사이트 크롤링 실정
   * clien.net
   * bobaedraem.co.kr


## 저작권
* 저작권법 허용
   * 단순 링크 - 사이트 대표 주소를 링크
   * 직접 링크 - 특정 게시물을 링크
* 저작권법 위반
   * 프레임 링크 - 저작물의 일부를 홈페이지에 표시
   * 임베드 링크 - 저작물 전체를 홈페이지에 표시


## 로봇 배제 표준(robots.txt)
* 웹사이트에 로봇이 접근하는 것을 방지하기 위한 규약
* 예제
   * 모두 허용
     > User-agent: *
     > Allow: /
   * 모두 차단
     > User-agent: *
     > Disallow: /
   * 다양한 조합
     > User-agent: googlebot  (googlebot 로봇만 적용)
     > Disallow: /private/    (이 디렉토리를 접근 차단)
     > User-agent: googlebot-news (googlebot-news 로봇만 적용)
     > Disallow: /            (모든 디렉토리를 접근 차단한다)
     > User-agent: *          (모든 로봇 적용)
     > Disallow: /something/  (이 디렉토리를 접근 차단)
* 실제 사이트의 robots.txt: 뽐뿌, 클리앙, SLR 클럽
   * 중고시장 관련된 대부분의 사이트는 로그인한 사용자만 접근허용 가능하니,
   * 왠만해서 그런 크롤링안하는 것이 좋음
   * 크롤링할지 말지에 대한 선택은 robots.txt 파일 내용 확인

크롤링은 적절히 delay를 주면 해당 사이트에 큰 무리를 주지 않을 수 있음

#### 뽐뿌 robots.txt 예제(크롤링할때 딜레이를 1초 주는것을 권고)
<pre>
User-agent: *
Crawl-delay: 1
Disallow: /include/
Disallow: /zboard/view.php?id=market
Disallow: /zboard/view.php?id=market_phone
Disallow: /zboard/view.php?id=market_social
Disallow: /zboard/view.php?id=cmarket
Disallow: /zboard/view.php?id=onmarket
Disallow: /zboard/view.php?id=market_story
Disallow: /zboard/view.php?id=gonggu
Disallow: /zboard/view.php?id=my
Disallow: /search_bbs.php
Disallow: /zboard/view_info2.php
Disallow: /bookmark/
Disallow: /chat
</pre> 

#### slrclub robots.txt 예제(User-Agent 전체 사이트 접근을 막고 있음)
<pre>
User-agent: Googlebot
Disallow:
User-agent: Googlebot*
Disallow:
User-agent: Mediapartners-Google*
Disallow: 
User-agent: ZumBot
Disallow: 
User-agent: Yeti
Disallow: 
User-agent: daumoa
Disallow: 
User-agent: KaBot
Disallow: 
User-Agent:*
Disallow:/ 
</pre>

- - -

## Scrapy 구조
* Scrapy 실행 명령
   * scrapy startproject "project name"

* Scrapy 동작
   * items 정의
   * 스타트 url 지정(start_requests, start_urls), callback 함수 지정(parse())
      * start_urls라는 url 리스트를 생성하는 방법 (스트링 리스트)
      * start_requests를 정의하는 방법
   * callback 함수 정의
      * selector(xpath, css)를 이용하여 데이터 선택
   * Pipeline을 이용하여 데이터를 필터링하거나 데이터베이스에 저장

spiders 폴더 내부에 실제 크롤링하는 로직이 위치하게 됨.
크롤링 대상 게시물들에 대한 게시물, 저작자, 제목, url 등을 items에 저장.
items에 저장된 데이터 기반으로 pipe라인에서 DB에 넣을지,
특별한 규칙에 의해 게시물을 필터링할것인지를 결정함

settings.py 파일의 경우, pipelines의 순서를 결정하거나,
로그 파일을 지정하고 로그파일 레벨도 지정 가능.

scrapy.cfg는 전체 프로젝트 배포시 관련 설정들에 대한 나열.


### Spiders
* 크롤러의 이름 지정
   * name
* 스타트 url 지정
   * start_urls
      * 시작 주소를 리스트 형태로 추가 가능
   * start_requests
      * 콜백함수를 지정할 수 있음
      * 사이트에 로그인할때 사용
* 파서 정의
   * def parse(self, response):

### Selector
* HTML 문서에 특정 노드를 선택하도록 지원하는 함수(쉽게)
   * css vs xpath selector

__특정 문자열 가져오기__
<pre>
$ response.xpath('//title/text()')
[<Selector (text) xpath=//title/text()>]
$ response.css('title::text')
[<Selector (text) xpath=//title/text()>]

$ response.xpath('//base/@href').extract()
[u'http://example.com/']

$ response.css('base::attr(href)').extract()
[u'http://example.com/']

$ response.xpath('//a[contains(@href, "image")]/@href').extract()
[u'image1.html',
 u'image2.html',
 u'image3.html'.
 u'image4.html',
 u'image5.html']

$ response.css('a[href*=image]::attr(href)').extract()
[u'image1.html',
 u'image2.html',
 u'image3.html',
 u'image4.html',
 u'image5.html']

$ response.xpath('//a[contains(@href, "image")]/imge/@src').extract()
[u'image1_thumb.jpg',
 u'image2_thumb.jpg',
 u'image3_thumb.jpg',
 u'image4_thumb.jpg',
 u'image5_thumb.jpg']

$ response.css('a[href*=image] img::attr(src)').extract()
[u'image1_thumb.jpg',
 u'image2_thumb.jpg',
 u'image3_thumb.jpg',
 u'image4_thumb.jpg',
 u'image5_thumb.jpg']
</pre>


### Pipeline
* 데이터를 크롤링한 이후에 특정 행동을 수행(크게 4가지 특성)
   * 데이터의 유효성 검사
   * 중복 체크
   * 데이터베이스에 아이템 저장
   * 필터링
* settings.py
   * 파이프 클래스 및 순서를 지정
<pre>
ITEM_PIPLINES = {
	// '클래스명':우선순위(낮은게 먼저 실행됨)
	'oneq.pipelines.CommunityPipeline':300,
}
</pre>


### Logging
* Settings.py
   * LOG_FILE='logfile.log'
   * LOG_LEVEL=logging.DEBUG
* Log Level
   1. logging.CRITICAL - for critical errors(highest severity)
   2. logging.ERROR - for regular errors
   3. logging.WARNING - for warning messages
   4. logging.INFO - for informational messages
   5. logging.DEBUG - for debugging messages(lowest severity)


