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


