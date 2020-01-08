#****************************************************************  
#coding=utf-8
# interfaceautotest.py  
# Author     : Liuyang  
# Version    : 1.1.3
# Date       : 2016-11-23
# Description: 接口自动化测试框架
#参考博文：http://www.nnzhp.cn/article/7/
#**************************************************************** 

import xlrd,os,logging,sys,requests,time,smtplib
from xlutils import copy
from email.mime.text import MIMEText
from email.header import Header
import ConfigParser

#强制设置默认编码方式
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

#日志打印功能
log_file = os.path.join(os.getcwd(),'log/sas.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def readExcel(file_name):
	testCaseFile = os.path.join(os.getcwd(),file_name)
	if not os.path.exists(file_name):
		logging.error('测试用例不存在！')
		logging.error('当前获取文件的目录是%s' %testCaseFile)
		sys.exit()
	testCase = xlrd.open_workbook(testCaseFile)
	sheet = testCase.sheet_by_index(0)
	rows = sheet.nrows
	case_list = []
	for i in range(rows):
		if i != 0:
			case_list.append(sheet.row_values(i))
			logging.info('第%d条用例内容是%s' %(i,case_list))
	interfacetest(case_list, file_name)

def interfacetest(case_list, file_name):
	res_flags = []
	request_urls = []
	responses = []

	for case in case_list:
		product = case[0]
		case_id = case[1]
		interface_name = case[2] 
		case_detail = case[3]
		method = case[4]
		url = case[5]
		param = case[6]           #需要加判断是否参数异常
		res_check = case[7]
		tester = case[9]

		'''
		if param == '':
			new_url = url
			request_urls.append(new_url)
		else:
			new_url = url + '?' + urlParam(param)
			request_urls.append(new_url)
		'''
		headers={"Content-Type": "application/json"}
		logging.info('下面执行第%d条测试用例' %case_id)

		if method.upper() == 'GET':
			logging.info('GET请求链接是%s, 参数是%s' %(url, param))
			r = requests.get(url, params = param)
			results = r.text
			logging.info('GET请求结果是%s' %results)
			responses.append(results)
			res = readRes(results, res_check)
			logging.info(res)
		elif method.upper() == 'POST':
			logging.info('POST请求链接是%s, 参数是%s' %(url, param))
			r = requests.post(url, headers = headers, data = param)
			results = r.text
			logging.info('POST请求结果是%s' %results)
			responses.append(results)
			res = readRes(results, res_check)
			logging.info(res)  #当预期结果字段为空的时候
		else:
			res = [] #此处定义res为后面判断用例是否失败  ，衔接第85行
			responses.append('Request style is wrong!!!') #当请求无结果的时候提供错误的结果
			logging.info('当前仅支持get和post请求，请检查用例id为%d的请求方式！' %case_id)
			logging.info('fail')

		if 'pass' in res:      #考虑重写判断函数
			res_flags.append('pass')
		else:
			res_flags.append('fail')

	copy_excel(file_name, res_flags, responses)

def readRes(res, res_check):
	if res_check == '':
		logging.error('预期结果字段为空，请补全!')
		return 'fail' #不进行return会出错，且提供为空情况下的log输出 见第78行
	else:
		for s in res_check:
			if s in res: #此处用in 确定是否为bug！！！
				pass
			else:
				return 'ERROR，返回结果与预期结果不一致！返回结果为 '+res+'\n预期结果为：'+res_check+'\nfail'
		return 'pass'

'''
判断待测试用例是否执行成功的函数2，见下图else分支：
需要import re
	else:
		try:
			pattern = re.compile(res_check)
			match = pattern.search(res)
			if match.group() == res_check:
				return 'pass'
		except AttributeError:
			return 'fail'
'''


def copy_excel(file_name, res_flags, responses):
	testCaseFile = os.path.join(os.getcwd(), file_name)
	testCase = xlrd.open_workbook(testCaseFile)
	new_testCase = copy.copy(testCase)
	sheet = new_testCase.get_sheet(0)

	i = 1
	for response, flag in zip(responses, res_flags):
		sheet.write(i, 8, u'%s' %response)
		sheet.write(i, 10, u'%s' %flag)
		i = i + 1

	global file_time #为解析结果文件预留
	file_time = time.strftime('%Y%m%d%H%M%S')
	new_testCase.save(os.path.join(os.getcwd(),'%s_testresult.xls' %file_time))

def getConf():
	conf_file = ConfigParser.ConfigParser()
	conf_file.read(os.path.join(os.getcwd(), 'config.ini'))
	conf = {}
	conf['sender'] = conf_file.get("email", "sender")
	conf['receiver'] = conf_file.get("email", "receiver")
	conf['smtpserver'] = conf_file.get("email", "smtpserver")
	conf['username'] = conf_file.get("email", "username")
	conf['password'] = conf_file.get("email", "password")
	return conf

def sendMail(text):
	mail_info = getConf()
	sender = mail_info['sender']
	receiver = mail_info['receiver'].split(',') #把字符串转换成smtp可识别的receiver列表
	subject = '[AutomationTest]接口自动化测试报告通知%s' %file_time
	smtpserver = mail_info['smtpserver']
	username = mail_info['username']
	password = mail_info['password']
	msg = MIMEText(text,'html','utf-8')
	msg['Subject'] = Header(subject, 'utf-8')
	msg['From'] = sender
	msg['To'] = ''.join(receiver)
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()

def analysisExcel():
	report_excel = os.path.join(os.getcwd(), '%s_testresult.xls' %file_time)
	if not os.path.exists('%s_testresult.xls' %file_time):
		logging.error('测试用例未生成，请检查！')
		sys.exit()
	testResult = xlrd.open_workbook(report_excel)
	sheet = testResult.sheet_by_index(0)
	rows = sheet.nrows
	result_list = []
	for i in range(rows):
		if i != 0:
			result_list.append(sheet.row_values(i))
	success_list = []
	fail_list = []
	for result in result_list:
		if result[10] == 'pass':
			success_list.append(result)
		elif result[10] == 'fail':
			fail_list.append(result)
		else:
			logging.info('用例执行结果回填状态有误，请检查！')
	html = '<html><body>接口自动化扫描，共有 ' + str(len(fail_list)) + ' 个异常接口，'  + str(len(success_list)) + '个成功接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
	for fail_result in fail_list:
		html = html + '<tr><td style="text-align:left">' + fail_result[2] + '</td><td style="text-align:left">' + fail_result[10] + '</td><td style="text-align:left">' + fail_result[5] + '</td><td style="text-align:left">' + fail_result[8] + '</td></tr>'
	for success_result in success_list:
		html = html + '<tr><td style="text-align:left">' + success_result[2] + '</td><td style="text-align:left">' + success_result[10] + '</td><td style="text-align:left">' + success_result[5] + '</td><td style="text-align:left">' + success_result[8] + '</td></tr>'
	return html

'''
def urlParam(param):

	return param.replace(';', '&')
'''


if __name__ == '__main__':
	readExcel('jiekouceshi.xlsx')
	html = analysisExcel()
	sendMail(html)
