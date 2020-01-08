# -*- coding: utf-8 -*-
from selenium import webdriver
import time
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://videojs.com/")
video = driver.find_element_by_xpath("//body/section[1]/div/video")
url = driver.execute_script("return arguments[0].currentSrc;", video)
print url
print("start")
driver.execute_script("return arguments[0].play()", video)
time.sleep(15)
print("stop")
driver.execute_script("return arguments[0].pause()", video)
driver.quit()

# driver = webdriver.Chrome()
# driver.get("http://videojs.com/")
#
# video = driver.find_element_by_xpath("//body/section[1]/div/video")
#
# # 返回播放地址文件
# time.sleep(20)
# url = driver.execute_script("return arguments[0].currentSrc;", video)
# print(url)
#
#
# # 播放视频
# print("start")
# driver.execute_script("return arguments[0].play()", video)
