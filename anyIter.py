#!/usr/bin/env python

class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe = safe
        self.iter = iter(data)
    def __iter__(self):
        return self
    def __next__(self,howmany=1): #python3 和 Python2 迭代器有一些区别
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

a = AnyIter(range(10))
i = iter(a)
for j in range(1,5):
    print(j,':',i.__next__(j))

