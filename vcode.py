# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


def send_mail(text):
        subject = 'vcode send report %s' % time.strftime("%Y-%m-%d %H:%M:%S")
        smtpserver = 'smtp.qiye.163.com'
        username = 'liuyang@axon.com.cn'
        password = 'pVSnSE89rfCp8zXR'
        sender = 'liuyang@axon.com.cn'
        receiver = ['liuyang@axon.com.cn', 'wangxm@axon.com.cn']
        msg = MIMEText(text, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = ';'.join(receiver)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()


def get_vcode(urllist, phonelist):
    success_url = []
    fail_url = {}
    for u in urllist:
        try:
            driver = webdriver.Chrome()
            driver.get(u)
            driver.maximize_window()
            # txts = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located(By.XPATH("//div[@class='txt']/img")))
            time.sleep(5)
            txts = driver.find_elements_by_xpath("//div[@class='txt']/img")

            txts[0].click()
            driver.find_element_by_class_name('weui-input').send_keys(phonelist[0])
            time.sleep(1)
            send_btn = driver.find_element_by_class_name('weui-btn')
            send_btn.click()
            time.sleep(1)
            assert send_btn.text.endswith(u'后获取'), "send_btn wasn't changed"
            driver.find_element_by_class_name('vux-close').click()
            success_url.append(u)
        except Exception as err:
            fail_url[u] = str(err)
        finally:
            driver.close()
            time.sleep(55)

    html = '''
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>短信发送测试结果</title>
            </head>
            <body>
            <p>需要校验的URL数量：%d </p>
            <p>发送成功数量：%d </p>
            <p>发送异常数量：%d </p>
            ''' % (len(urllist), len(success_url), len(fail_url))

    errhtml = ''
    for adress, errmsg in fail_url.items():
        errhtml += '<p>异常地址：%s , 对应错误信息：%s</p>' % (adress, errmsg)

    endhtml = '</body></html>'
    send_mail(html + errhtml + endhtml)

if __name__ == '__main__':
    url = ['http://www.kk186.cn/cib_creditcard_v2/go/1?channel=yd', 'http://www.kk186.cn/cib_creditcard_v2/go/2?channel=yd', 'http://www.kk186.cn/cib_creditcard_v2/go/3?channel=yd', 'http://www.kk186.cn/cib_creditcard_v2/go/4?channel=yd', 'http://www.kk186.cn/cib_creditcard_v2/go/5?channel=yd', 'http://www.js165.com/cib_creditcard_v2/go/6?channel=lt_wx', 'http://www.js165.com/cib_creditcard_v2/go/7?channel=lt_wx', 'http://www.js165.com/cib_creditcard_v2/go/8?channel=lt_wx', 'http://www.js165.com/cib_creditcard_v2/go/9?channel=lt_wx', 'http://www.js165.com/cib_creditcard_v2/?channel=lt_wx_qk']
    # url = ['http://www.js165.com/cib_creditcard_v2/?channel=lt_wx_qk']
    phone = ['18651687312']
    get_vcode(url, phone)
