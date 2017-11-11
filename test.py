from urllib.request import urlopen

class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat,cls).__new__(cls,round(val,2)) #四舍五入

#可变类型的例子
class SortedKeyDict(dict):
    #def __init__(self):
     #   self.foo = 100
    def keys(self):
        return sorted(super(SortedKeyDict,self).keys())

num = RoundFloat(1.5955)
print(num)

d = SortedKeyDict((('zheng-cai',67),('hui-jun',68),('xin-yi',2)))
print('By iterator:'.ljust(12),[key for key in d])
print('By keys():'.ljust(12),d.keys())
print(issubclass(SortedKeyDict,RoundFloat)) # sub,sup(sup可以是一个可能父类的元组) 判断一个类是另一个类的子类或子孙类
print(isinstance(d,SortedKeyDict)) #判断一个对象是否是另一个类给定的实例
print(isinstance(4,int))
print(isinstance(4,(float,str,list)))
print(hasattr(SortedKeyDict,'keys'))
#print(getattr(SortedKeyDict,'foo'))
