import random
# spnum = ['106557392', '106557392025', '106557392512', '106557392510', '106557392519', '106557392511', '106557392513', '106557392516', '106557392523', '106557392515']

f = open(r'C:\Users\Administrator\Desktop\users-1w.txt', 'w')
# 200000
for i in range(10000):
    phone = 18626330614 + i
    f.write(str(phone) + "\n")
f.close()
