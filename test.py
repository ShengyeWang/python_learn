from urllib.request import urlopen

class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat,cls).__new__(cls,round(val,2)) #四舍五入

num = RoundFloat(1.5955)
print(num)
