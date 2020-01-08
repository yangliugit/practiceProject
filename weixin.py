# -*- coding=utf-8 -*-
import itchat, time, sys
reload(sys)
sys.setdefaultencoding("utf-8")
# 微信定时发送消息简版
itchat.auto_login(hotReload=True)
# name后填微信备注即可
users = itchat.search_friends(name=u'李俊')
# 获取对方UserName
print(users)
#for i in range(100):
#   time.sleep(10)
itchat.send(u'dajun, come on, bite me', toUserName="filehelper")
# itchat.send(u'old two, come on.bite me', toUserName=u'@40159058a8eef93b7b135886ec572805')
# itchat.run()
