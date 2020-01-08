# -*-coding: utf-8 -*-
from __future__ import division
import math
import cmath


print 10//4
print 10 % 3
print -3**2
print -(3**2)
# 向前取整，强制转换为int类型
print int(math.floor(1.99))
# 向后取整，强制转换为int类型
print int(math.ceil(1.11))
# 取平方根
print math.sqrt(1)
# 求虚数平方根
print cmath.sqrt(-1)
# raw_input()和input()区别在于输入限制
# name = raw_input("what is your name?\n")
# print "hello\' " + name
print 1000L
# 输出更能被理解的字符串
print "hello,world"
# 输出程序字符串
print repr("hello world!")

temp = 42
print "the temperature is " + str(42)
# longstring,其中换被忽略了
print '''this\
 is long\
 string\
'''
print r"'''sss'''"

print u"hello world"

su = "人生苦短"

a = "ste"
print a

print pow(9, 3)
# 通用序列操作
string1 = "hello"
print string1[-5]
# user_input = raw_input("please input this year")[3]
# print user_input


def datechange(year, month, day):
    months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

    month_name = months[month - 1]
    ordinal = repr(day) + endings[day - 1]
    return month_name + ' ' + ordinal + '. ' + repr(year)

# if __name__ == '__main__':
#     datestring = datechange(2017, 12, 25)
#     print datestring
