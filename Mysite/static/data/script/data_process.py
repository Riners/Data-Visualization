#!/usr/bin/python
#coding:utf-8
import sys
import time
import MySQLdb
from MySQLdb import IntegrityError
import urllib.request
from math import log
from pdb import set_trace
from Queue import Queue
from os.path import exists
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
# reload(sys)
sys.setdefaultencoding( "utf-8" )
HOSTNAME = 'localhost'
DATABASE = 'tabaoip'
USERNAME = 'root'
PASSWORD = 'zhxfei..192'
DBURI = 'mysql://{}:{}@{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
TABLENAME= 'c_ip_addr_info'
con = MySQLdb.connect(HOSTNAME,USERNAME,PASSWORD,DATABASE,charset="utf8")
def into_db(c_ip,mask,c_area,c_city,c_isp,c_area_id,c_city_id,c_isp_id):
    sql_content = "insert into {} values ('{}',{},'{}','{}','{}',{},{},{})".format(
                                TABLENAME,c_ip,mask,c_area,c_city,c_isp,
                                            c_area_id,c_city_id,c_isp_id)
    with con as cur:
        try:
            cur.execute(sql_content)
        except IntegrityError:
            pass
def db_test():
    sql_content = 'desc {}'.format(TABLENAME)
    with con as cur:
        cur.execute(sql_content)
        for line in cur.fetchall():
            print (line)
def ip_resolve(ip,mask):
    '''resolve isp_name use ip.taobao.com'''
    # print 'ip_resolve execute {}'.format(ip)
    r = requests.get(
        'http://ip.taobao.com/service/getIpInfo.php?ip={}'.format(
                                                        ip,timeout=0.1))
    if r.status_code == 200 and r.json().get('code') == 0:
        data = r.json()
        c_ip   = data['data']['ip']
        c_area = data['data']['area']
        c_city = data['data']['city']
        c_isp  = data['data']['isp']
        c_area_id = int(data['data']['area_id']) if data['data']['area_id'] else -1
        c_city_id = int(data['data']['city_id']) if data['data']['city_id'] else -1
        c_isp_id  = int(data['data']['isp_id']) if data['data']['isp_id'] else -1
        res_q.put((c_ip,mask,c_area,c_city,c_isp,c_area_id,c_city_id,c_isp_id))
    # elif retry_num>0:
    #     count = retry_num - 1
    #     return ip_resolve(ip,mask,count)
    else:
        return ip_resolve(ip,mask)
def net_catch():
    '''find the network segment and netmask from src.html'''
    with open('src.html', 'r') as f:
        for line in f:
            if line.startswith('apnic|CN|ipv4'):
                '''
                the line example:
                    apnic|IN|ipv4|103.27.84.0|1024|20130701|assigned
                '''
                net,cnt =  line.strip().split('|')[3:5]
                yield net,int(32-log(float(cnt))/log(2))
def sql_worker(res_q):
    while True:
        data = res_q.get()
        # if data:
        c_ip,mask,c_area,c_city,c_isp,c_area_id,c_city_id,c_isp_id = data
        into_db(c_ip,mask,c_area,c_city,c_isp,c_area_id,c_city_id,c_isp_id)
        print ('{} insert OK'.format(c_ip))
        res_q.task_done()
t = time.time()
res_q = Queue()
t = Thread(target=sql_worker,args=(res_q,))
t.daemon = True
t.start()
tasks = []
for ip,mask in net_catch():
    task = Thread(target=ip_resolve,args=(ip,mask,))
    task.start()
    tasks.append(task)
for task in tasks:
    task.join()
print ('tasks over!')
res_q.join()
#db_test()
print ("All done,Cost : {}".format(time.time() - t))