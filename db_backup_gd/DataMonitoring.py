#!/disk/env/py3env/bin python3.6
# -*- coding:utf-8 -*-
import pymongo
from pymongo import MongoClient,MongoReplicaSetClient

from mongoengine import *
from optparse import OptionParser
from pymongo import MongoClient
import models
from bson.objectid import ObjectId
import time
from datetime import date, datetime, timedelta
from mongoengine.queryset.visitor import Q
import sys
import os
import argparse
import re
import glob
import json
import time

##connect database
def connect():
	client = MongoReplicaSetClient("10.100.15.30:27017,10.100.15.31:27017,10.100.15.32:27017")
	db=client.gd
	return db
##connect database
#connect('gd', host='10.100.15.30', port=27017)
#print ("success !")

def work():
	DB_data=[]
	collection = connect().GD_WES_CLINIC
	count = collection.find().count()
	for item in collection.find():
			DB_data.append(item)
	startDate=''
	endDate=''
	today=datetime.now().strftime("%Y-%m-%d")
	yesterday=(datetime.now()+timedelta(days=-1)).strftime("%Y-%m-%d")
	if yesterday == '':
		s = "1970-01-01 00:00:00"
	else:
		s = yesterday + " 00:00:00"
	if today == '':
		now = datetime.now()
		e = now.strftime("%Y-%m-%d %H:%M:%S")
	else:
		e = today + " 00:00:00"
	s_arr = time.strptime(s, '%Y-%m-%d %H:%M:%S')
	e_arr = time.strptime(e, '%Y-%m-%d %H:%M:%S')

	s_time = int(time.mktime(s_arr))
	e_time = int(time.mktime(e_arr))
	print ('CAl_Start:',s,s_time)
	print ('CAl_End:',e,e_time)
	##queryset转换成list,过滤不符合条件的数据
	
	entry_list = DB_data
	new_DB=[]
	filter_id=[]
	query_id=[]
	all_id=[]
	for m in entry_list:
		oid = m['_id']
		all_id.append(str(oid))
		a = ObjectId(oid)
		b = time.strftime("%Y-%m-%d %H:%M:%S", a.generation_time.timetuple())
		timeArray = time.strptime(b, '%Y-%m-%d %H:%M:%S')
		d_time = int(time.mktime(timeArray))
		#print ('TT:',d_time,s_time,e_time)
		if d_time >= s_time and d_time <= e_time:
			query_id.append(str(oid))
			continue
		else:
			filter_id.append(str(oid))
	'''print ('LEN:',len(entry_list))
	print ('FLEN:',len(filter_id))
	print ('QLEN:',len(query_id))
	print('ALL:',all_id)
	print ('QID:',query_id)'''
	storage_time_dict=[]
	for item in entry_list:
		oid=item['_id']
		a = ObjectId(oid)
		b = time.strftime("%Y-%m-%d %H:%M:%S", a.generation_time.timetuple())
		timeArray = time.strptime(b, '%Y-%m-%d %H:%M:%S')
		d_time = int(time.mktime(timeArray))
		#storage_time_dict[oid]=d_time
		#print ('FFF:',item['_id'])
		if str(oid) in query_id:
			new_DB.append(item)
			continue
			
	print ('NLEN:',len(new_DB))
	for m in new_DB:
		print ('SS:',m['bus_code'])
def runTask(func,day=0,hour=0,min=0,second=0):
	now=datetime.now()
	iter_now_time=""
	while True:
		iter_now=datetime.now()
		####一天扫两次
		if(iter_now.hour==1):
		#if(iter_now.hour==1 or iter_now.hour==9 or iter_now.hour==10 or iter_now.hour==11 or iter_now.hour==12 or iter_now.hour==13 or iter_now.hour==14):
			print ('NOW Time:',iter_now.hour)
			print ("Start work:%s"%datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			func()
			print ("End work:%s"%datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
			print ("####################################################")
			time.sleep(1*3600)
		else:
			print ("Waiting")
			time.sleep(int(1*3600))
if  __name__=="__main__":
	#work()	
	runTask(work,hour=24)