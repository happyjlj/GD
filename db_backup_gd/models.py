#coding:utf-8

from django.db import models
from mongoengine import *

#。db里面的表的命名的方式为：类_表名。例如：WebServer_Template_1，下方只填写表名。
# ID为主键，不需要定义； name 类型为字符串，长度为30，值为唯一 ； selected为布尔值。

class GD_WES_CLINIC(Document):
	bus_code = StringField(max_length=200)
	isoverseas = StringField(max_length=200)
	subfamilyContents = StringField(max_length=200)
	karyotype = StringField(max_length=200)
	Doctor = StringField(max_length=200)
	panelproject = StringField(max_length=200)
	inspectnbr = StringField(max_length=200)
	reportresult = StringField(max_length=200)
	birthday = StringField(max_length=200)
	sex = StringField(max_length=200)
	urgent = StringField(max_length=200)
	special_memo = StringField(max_length=200)
	istestcnv = StringField(max_length=200)
	family_test = StringField(max_length=200)
	antenatal = StringField(max_length=200)
	sam_type = StringField(max_length=200)
	city = StringField(max_length=200)
	imagepath = StringField(max_length=200)
	istestpanel = StringField(max_length=200)
	sub_test_items = StringField(max_length=200)
	certnbr = StringField(max_length=200)
	report_director = StringField(max_length=200)
	hospital = StringField(max_length=200)
	pro_code = StringField(max_length=200)
	internalresult = StringField(max_length=200)
	isrebloods = StringField(max_length=200)
	checktime = StringField(max_length=200)
	location = StringField(max_length=200)
	family_verify = StringField(max_length=200)
	receive_date = StringField(max_length=200)
	leveltime = StringField(max_length=200)
	hosp_caseid = StringField(max_length=200)
	province = StringField(max_length=200)
	rptmodes = StringField(max_length=200)
	urgentmemo = StringField(max_length=200)
	patient = StringField(max_length=200)
	lastupdatetime = StringField(max_length=200)
	rptlngtypes = StringField(max_length=200)
	subnumber = StringField(max_length=200)
	rptclinicinfo = StringField(max_length=200)
	checksex = StringField(max_length=200)
	fastqtime = StringField(max_length=200)
	gestation = StringField(max_length=200)
	body_check = StringField(max_length=200)
	report_version = StringField(max_length=200)
	check_hospital = StringField(max_length=200)
	expand = StringField(max_length=200)
	customer = StringField(max_length=200)
	recvusers = StringField(max_length=200)
	clinicfile = StringField(max_length=200)
	name = StringField(max_length=200)
	casetypes = StringField(max_length=200)
	misbirth = StringField(max_length=200)
	takebloodtime = StringField(max_length=200)
	age = StringField(max_length=200)
	test_item = StringField(max_length=200)
	other_test = StringField(max_length=200)
	resultexp = StringField(max_length=200)
	cnv_caseid = StringField(max_length=200)
	appendix = StringField(max_length=200)
	Deadline = StringField(max_length=200)
	oldcaseid = StringField(max_length=200)
	clinical_infor = StringField(max_length=200)
	samplestatus = StringField(max_length=200)
	deliverytypes = StringField(max_length=200)
	panelprojectnew = StringField(max_length=200)
	reportexplain = StringField(max_length=200)
	checkstatus = StringField(max_length=200)
	reportexplain_wes = StringField(max_length=200)
	reportresult_wes = StringField(max_length=200)
	ICF_version = StringField(max_length=200)
	additional_infor = StringField(max_length=200)
	acquisition_date = StringField(max_length=200)

    # ReferenceField相当于foreign key
    # qc_id = ReferenceField('Test1',reverse_delete_rule=CASCADE)
    # meta = {'allow_inheritance': True}