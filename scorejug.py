# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender in ('male', 'female'):
            self.__gender = gender
        else:
            print "gender isn't normal type!"
            
'''        
if __name__ == '__main__':
    bart = Student('bart', 'dmale')
    if bart.get_gender() != 'male':
        print 'test failed!'
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print 'test failed'
        else:
            print 'test success!'
'''
