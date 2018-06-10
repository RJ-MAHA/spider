# -*- coding: utf-8 -*-

# Scrapy settings for zgcpwsw project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zgcpwsw'
SPIDER_MODULES = ['zgcpwsw.spiders']
NEWSPIDER_MODULE = 'zgcpwsw.spiders'
RETRY_HTTP_CODES = [500, 503, 504, 400, 408]
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY =2
DOWNLOADER_MIDDLEWARES = {
    'zgcpwsw.middlewares.ZgcpwswDownloaderMiddleware': 544,
    #     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
    #     'zgcpwsw.middlewares.ProxyMiddleWare':125,
    #     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None

    'zgcpwsw.middlewares.UserAgentMiddleware': 200,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    #	  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    #'zgcpwsw.middlewares.ProxyMiddleware': 100,

    'scrapy_crawlera.CrawleraMiddleware': 600


}

ITEM_PIPELINES = {
    #    'zgcpwsw.pipelines.ZgcpwswPipeline': 300,
    'zgcpwsw.pipelines.wenshu_Pipeline': 300,
    'zgcpwsw.pipelines.Pipeline_ToCSV':100

}
DOWNLOAD_TIMEOUT = 60

DEPTH_PRIORITY = 0
REDIRECT_ENABLED = True
CONCURRENT_REQUESTS = 5
RETRY_ENABLED =     True
RETRY_TIMES = 10

"""
SET YOUR DATABASE INFOMATION HERE
"""


HEADER_DEFULT = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"wenshu.court.gov.cn",
    "Referer":"http://wenshu.court.gov.cn/list/list/",
    "User-Agent":"Scrapy/1.5.0 (+https://scrapy.org)",
    "Upgrade-Insecure-Requests":"1"
}
HEAD = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_gscu_2116842793=26394928v73dks64; __utmz=61363882.1526458934.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=61363882.851881720.1526458934.1526609543.1526912978.3; Hm_lvt_9e03c161142422698f5b0d82bf699727=1527125964; _gscu_125736681=271340148lsiwm43; wzwsconfirm=cf57bf1e060599ee428a6ff6e813dd46; wzwstemplate=MQ==; ccpassport=52ec30bbe0ba045d61a5b23cfb9b1305; wzwschallenge=-1; wzwsvtime=1527818656; Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1527572896,1527649501,1527666623,1527818929; ASP.NET_SessionId=v3avoeumhfillgkbanf311wm; _gscbrs_2116842793=1; Hm_lpvt_3f1a54c5a86d62407544d433f6418ef5=1527819765; vjkl5==",
    "Host": "wenshu.court.gov.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}
LOG_LEVEL = 'INFO'
COOKIE_DEFULT = "_gscu_2116842793=26394928v73dks64; __utmz=61363882.1526458934.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=61363882.851881720.1526458934.1526609543.1526912978.3; Hm_lvt_9e03c161142422698f5b0d82bf699727=1527125964; _gscu_125736681=271340148lsiwm43; Hm_lvt_3f1a54c5a86d62407544d433f6418ef5=1527649501,1527666623,1527818929,1527834380; _gscs_2116842793=t27836587vchiin25|pv:5; vjkl5="