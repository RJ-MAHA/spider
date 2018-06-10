# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os

import pymysql
from twisted.enterprise import adbapi
import datetime
import  logging

class ZgcpwswPipeline(object):
    def process_item(self, item, spider):
        return item

class wenshu_Pipeline(object):
	def __init__(self, dbpool):
		self.dbpool = dbpool

	@classmethod
	def from_settings(cls, settings):
		dbparms = dict(host=settings["MYSQL_HOST"],
					   db=settings["MYSQL_DB"],
					   user=settings["MYSQL_USER"],
					   passwd=settings["MYSQL_PASSWORD"],
					   charset="utf8",
					   cursorclass=pymysql.cursors.DictCursor,
					   use_unicode=True
					   )
		dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
		return cls(dbpool)

	def process_item(self, item, spider):

		query = self.dbpool.runInteraction(self.do_process, item)
		query.addErrback(self.handle_error)

	def handle_error(self, failure):
		print(failure)

	def do_process(self, cursor, item):

		cu = cursor.execute("select DOC_ID from T_YQ_WENSHU where DOC_ID = %s and SEARCH_KEY = %s",(item['docid'],item['searchKey']))

		if cu:
				    cursor.execute("update T_YQ_WENSHU  set TITLE =%s ,PUB_DATE=%s ,HTML=%s ,COURT= %s,CASE_TYPE=%s ,TRIAL_ROUND= %s,TRIAL_DATE= %s ,APPELLOR= %s,SEARCH_KEY=%s where DOC_ID = %s",(item['title'],item['pubdate'],item['html'],item['court'],item['caseType'],item['trialRound'],item['trialDate'],item['appellor'],item['searchKey'],item['docid']))
				    logging.info('update success:'+item['docid'])
		else:
				    cursor.execute("insert into T_YQ_WENSHU (DOC_ID,TITLE,PUB_DATE,HTML,COURT,CASE_TYPE,TRIAL_ROUND,TRIAL_DATE,APPELLOR,SEARCH_KEY,CREATE_DATE) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['docid'],item['title'],item['pubdate'],item['html'],item['court'],item['caseType'],item['trialRound'],item['trialDate'],item['appellor'],item['searchKey'],datetime.datetime.now()))
				    logging.info('insert table success:'+item['docid'])



class Pipeline_ToCSV(object):

	def process_item(self,item,spider):
		#判断字段值不为空再写入文件
		if item['docid']   and  item['title']   and  item['pubdate']   and  item['html']   and  item['court']   and  item['caseType']   and  item['trialRound']   and  item['trialDate']   and  item['appellor']   and  item['searchKey']   :
			ct = datetime.datetime.now().strftime('%Y-%m-%d')
			csv_filename = '/WENSHU_'+str(ct)+'.csv'
			store_file = os.path.dirname(__file__) + csv_filename
			if os.path.exists(store_file):
				logging.info("exists this file:"+store_file)
			else:
				file = open(store_file,'a+',newline='')
				writer = csv.writer(file)
				writer.writerow(['DOC_ID','TITLE','PUB_DATE','HTML','COURT','CASE_TYPE','TRIAL_ROUND','TRIAL_DATE','APPELLOR','SEARCH_KEY','CREATE_DATE'])
				file.close()
				logging.info("no this file:"+store_file)
			file = open(store_file,'a+',newline='')
			writer = csv.writer(file)
			writer.writerow([item['docid'],item['title'],item['pubdate'],item['html'],item['court'],item['caseType'],item['trialRound'],item['trialDate'],item['appellor'],item['searchKey'],datetime.datetime.now()])
			file.close()
		return item

