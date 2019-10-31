#!/disk/env/py3env/bin python3.6
# -*- coding:utf-8 -*-
from mongoengine import *
from optparse import OptionParser
from pymongo import MongoClient
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
#connect('wes_wgs', host='10.100.6.7', port=27017, username='wuser',password='berry2012')
#print ("success !")

def work():
	print ('START WORKING ... \n')
	
def runTask(func,day=0,hour=0,min=0,second=0):
	now=datetime.now()
	iter_now_time=""
	while True:
		iter_now=datetime.now()
		####一天扫两次
		print ('NOW Time:',iter_now.day)
		print ("Start work:%s"%datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		suffix=datetime.now().strftime("%Y-%m-%d")
		#func()
		commd1 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_CLINIC --out clinic."+suffix+".json"
		os.system(commd1)
		'''commd2 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_RESULT --out coresnv."+suffix+".json"
		os.system(commd2)
		commd3 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NOTE --out note."+suffix+".json"
		os.system(commd3)
		commd4 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_VUS --out corecnv."+suffix+".json"
		os.system(commd4)
		commd5 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_EXTEND --out extend_data."+suffix+".json"
		os.system(commd5)
		commd6 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_NE_APPENDIX --out negative_appendix."+suffix+".json"
		os.system(commd6)
		commd7 = "mongoexport --host 10.100.15.30 --db gd --collection GD_WES_SUPPLEMENT_REPORT --out supplement_report."+suffix+".json"
		os.system(commd7)'''
		print ("End work:%s"%datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print ("####################################################")
if  __name__=="__main__":
	#work()	
	runTask(work,hour=24)