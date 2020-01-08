# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome()
url = 'https://emumo.xiami.com/play?ids=/song/playlist/id/72395/object_name/default/object_id/0#loaded'
browser.get(url)
sleep(2)
# browser.maximize_window()
dot = browser.find_element_by_class_name("player-dot")
print(dot)

action = ActionChains(browser)
action.click_and_hold(dot).drag_and_drop_by_offset(dot, 400, 833).perform()
# sleep(1)
# # 坐标通过js document.getElementById("J_playerDot").getBoundingClientRect() 获取
# action.drag_and_drop_by_offset(dot, 360, 833).perform()
# # action.move_to_element_with_offset(dot, 360, 833).perform()
# action.click()
