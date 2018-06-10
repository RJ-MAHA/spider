import pandas
import pymysql
import scrapy
import re
import json
import demjson
from zgcpwsw.items import ZgcpwswItem
from scrapy.conf import settings

host=settings["MYSQL_HOST"]
db=settings["MYSQL_DB"]
user=settings["MYSQL_USER"]
passwd=settings["MYSQL_PASSWORD"]
port=settings["MYSQL_PORT"]

conn = pymysql.connect(host=host,user=user, passwd=passwd, db=db, charset='utf8')
cur = conn.cursor()
sql = "SELECT COMPANY_NAME from T_YQ_COMPANY"
cur.execute(sql)
get_names = cur.fetchall()
cur.close()
conn.close()
names = list(set(get_names).difference(tuple('NULL')))
names.sort()

class WswSpider(scrapy.Spider):
    name = "Wsw"
    Cookie = ""
    vjkl5 = ""
    vl5x = ""
    number = ""
    guid = ""
    start = 0
    end = 0

    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end


    def start_requests(self):
        i =1
        for name in names[int(self.start):int(self.end)]:
            name = name[0]
            yield scrapy.FormRequest(
                                url = 'http://wenshu.court.gov.cn/List/ListContent',
                                meta={'i':i,'name':name},
                                formdata = {"Param": "全文检索:"+name,
                                            "Index": str(i),
                                            "Page": "20",
                                            "Order": "法院层级",
                                            "Direction": "asc",
                                            "vl5x":str(self.vl5x) ,
                                            "number": self.number,
                                            "guid": str(self.guid)

                                            },
                                callback = self.parse_ListContent
                            )

    def parse_ListContent(self, response):
        body = bytes.decode(response.body)
        print(response.body)
        result = body.split("文书ID\\\":\\\"")
        for r in result:
                rt  = r.split("\\\",\\\"")
                for r1 in rt:
                    if re.match("[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}",r1):
                       print(r1,'\n')
                       yield scrapy.Request(url='http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID='+r1, meta={'DocID': r1,'i':0,'searchKey':response.meta['name']},dont_filter=True,callback=self.parse_doc)
        

    def parse_doc(self, response):
        try:
            item = ZgcpwswItem()
            item['docid'] = response.meta['DocID']
            item['searchKey'] = response.meta['searchKey']
            item['court'] = ''
            item['caseType'] = ''
            item['reason'] = ''
            item['trialRound'] = ''
            item['trialDate'] = ''
            item['appellor'] = ''
            str_jsonHtmlData = bytes.decode(response.body).split("jsonHtmlData = ")[1].split("\n")[0]
            str_jsonHtmlData = str_jsonHtmlData[1:-3]
            dict_jsonHtmlData = json.loads(str_jsonHtmlData.replace("\\","").replace("\n",""))
            print(dict_jsonHtmlData["Title"])
            item['title'] = dict_jsonHtmlData["Title"].encode('utf-8').decode('utf-8')
            print(dict_jsonHtmlData["PubDate"])
            item['pubdate'] = dict_jsonHtmlData["PubDate"].encode('utf-8').decode('utf-8')
            print(dict_jsonHtmlData["Html"])
            item['html'] = dict_jsonHtmlData["Html"].encode('utf-8').decode('utf-8')
            array_RelateInfo = bytes.decode(response.body).split("RelateInfo: [")[1].split("],LegalBase")[0].replace("},{","}},{{").split("},{")
            for i in array_RelateInfo:
                    dict_RelateInfo =   demjson.decode(i)
                    print(dict_RelateInfo["name"])
                    if dict_RelateInfo["key"] == 'court':
                        try:
                            item['court'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['court'] = ''
                    elif dict_RelateInfo["key"] == 'caseType':
                        try:
                            item['caseType'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['caseType'] = ''
                    elif dict_RelateInfo["key"] == 'caseTypecaseType':
                        try:
                            item['reason'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['reason'] = ''
                    elif dict_RelateInfo["key"] == 'trialRound':
                        try:
                            item['trialRound'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['trialRound'] = ''
                    elif dict_RelateInfo["key"] == 'trialDate':
                        try:
                            item['trialDate'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['trialDate'] = ''
                    elif dict_RelateInfo["key"] == 'appellor':
                        try:
                            item['appellor'] = dict_RelateInfo["value"].encode('utf-8').decode('utf-8')
                        except Exception as e:
                            item['appellor'] = ''
            yield item
        except Exception as e :
            print(e)
            return



