# -*- coding: utf-8 -*-
import pymysql
import sys
from scrapy import cmdline
from math import ceil
import time
from multiprocessing import Process

"""
SET YOUR DATABASE INFOMATION HERE
"""
name = 'Wsw'
conn = pymysql.connect(host=MYSQL_HOST,port =MYSQL_PORT ,user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset='utf8')
cur = conn.cursor()
sql = "SELECT count(*) from T_YQ_COMPANY"
cur.execute(sql)
c_count = cur.fetchall()[0][0]
cur.close()
conn.close()

if c_count > 0 and c_count:
    start = 1
    end = c_count
else:
    sys.exit(0)

def f(name,start,end):

    cmd = 'scrapy crawl {0} -a start={1} -a end={2}  -s LOG_FILE=wenshu.log'
    cmd = cmd.format(name,start,end)
    cmdline.execute(cmd.split())

if __name__ == '__main__':
    for i in range(int((ceil(start)+1)/200)+1,int((ceil(end)+1)/200)+1):
        p = Process(target=f, args=(name,(i-1)*200,i*200))
        p.start()
        time.sleep(1)
        p.join()




