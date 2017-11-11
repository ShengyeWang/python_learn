#!/usr/bin/env python

class NumStr(object):
    def __init__(self,num=0,string=''):
        self.__num = num
        self.__string = string
    def __str__(self):
        return '[%d::%r]'%(self.__num,self.__string)
    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other,NumStr):
            return self.__class__(self.__num + other.__num,self.__string + other.__string)
        else:
            raise TypeError
            'ILLegal argument type for built-in operation'

    def __mul__(self, num):
        if isinstance(num,int):
            return self.__class__(self.__num*num,self.__string*num)
        else:
            raise TypeError
            'ILLegal argument type for built-in operation'
    def __nonzero__(self):
        return self.__num or len(self.__string)
    def __norm_cval(self,cmpres):
        return cmp(cmpres,0)
    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num,other.__num)) + \
               self.__norm_cval(cmp(self.__string,other.__string))

a = NumStr(3,'foo')
b = NumStr(3,'goo')
c = NumStr(2, 'foo')
d = NumStr()
e = NumStr(string='boo')
f = NumStr(1)
print(a + b)
print(a*5)
print(d)
print(e)
print(f)
if (a == a):
    print(True)
if (a != b):
    print(True)
#result = a > b
#print(result)

##!!!!遗留问题
##!!!!比较大小时出错