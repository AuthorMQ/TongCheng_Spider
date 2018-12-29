# -*- coding: utf-8 -*-

# Scrapy settings for hangzhouhotel project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Baiduspider'

SPIDER_MODULES = ['hangzhouhotel.spiders']
NEWSPIDER_MODULE = 'hangzhouhotel.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hangzhouhotel (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Host": "www.ly.com",
        "Connection": "keep - alive",
        "Content - Length": "420",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "http://www.ly.com",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
        "Content - Type": "application / x - www - form - urlencoded;charset = UTF - 8",
        "Referer": "http://www.ly.com/searchlist.html?cityid=385",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "Hm_lvt_64941895c0a12a3bdeb5b07863a52466=1545811659; Hm_lvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1545810754,1545815723,1545828100; qdid=-9999; 17uCNRefId=RefId=0&SEFrom=&SEKeyWords=; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; CNSEInfo=RefId=0&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; __tctma=144323752.1545810753890123.1545810753214.1545810753214.1545828097747.2; __tctmu=144323752.0.0; __tctmz=144323752.1545828097747.2.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1545810753890123; __tctrack=0; Hm_lvt_f97c1b2277f4163d4974e7b5c8aa1e96=1545810755,1545815723,1545828100; wangba=1545828099948; GnHotelData=%7B%22CnHotelComeDate%22%3A%222018-12-26%22%2C%22CnHotelLeaveDate%22%3A%222018-12-27%22%2C%22CnHotelCityName%22%3A%22%25E5%2598%2589%25E5%2585%25B4%22%2C%22CnHotelCityId%22%3A%22385%22%2C%22CnHotelParCityId%22%3A%220%22%2C%22Keyword%22%3A%22%22%2C%22KeywordId%22%3A%220%22%2C%22KeywordType%22%3A%220%22%2C%22Longitude%22%3A%22%22%2C%22Latitude%22%3A%22%22%7D; td_sid=MTU0NTgzMDM0Myw1MDI0ZTcxZjcwYTEyNzNhODQzZmNiMWY1NDExMTNiY2I0ZGYxYTNkZDQ0NzNkZWViODcyMjZmZjkwZmRiMTY3LDJlMTFiYzI1Zjk0N2U5NjJhN2Q0OWEyMzQ3MDRhYmJmYWZmYjg1YTA2MzNiNjk3NjliMGEwYmUzYWRjN2FmNGI=; k_st=112.10.158.225|1545830343; td_did=3zLaMsROfzm32W%2FgRIHt9TTHe1q9Ky7ONULWFOQxbgL8yV1CQFBl%2FLSu54Zhpe8sJDloSlsa2CmTV1ScPqMZ7vD%2FGieTWrqR6imvqBWQTLKm20%2FDXzrqmDRgqVPtUZYKoV51%2FQ%2FSka%2FYokCPTaWq%2FoGq6wWezh5CxV%2FPCR15NpHnf3DIreZCE19AIMhzVRYRTG16sWV6RxJ2%2ByPrYSMebp4BtlbRX5%2Fsg11LLr%2FTKDcUZdrrePzfivm7FYHblJy%2F; t_q=1545830344349; __tctmc=144323752.205661717; __tctmd=144323752.737325; __tctmb=144323752.2884043894639891.1545831264853.1545831410114.11; Hm_lpvt_c6a93e2a75a5b1ef9fb5d4553a2226e5=1545831432; Hm_lpvt_f97c1b2277f4163d4974e7b5c8aa1e96=1545831432; route=91ae9a7c67227eae48420befaa4490da",
    }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hangzhouhotel.middlewares.HangzhouhotelSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'hangzhouhotel.middlewares.RandomProxyMiddleware': 555,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'hangzhouhotel.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_URI = 'localhost'
MONGO_DATABASE = 'hzhotel'
PROXY_URL = 'http://www.yooongchun.com:9999/?name=yooongchun&password=121561&method=random'