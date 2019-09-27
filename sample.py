#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import cgi
import sys
import io
import test
from tests import aaa

print("")

bb = aaa.AAA()
bb.test()

class MySampleClass:
    def __init__(self):
        self.aaa = "こんばんは<br>"
    def myfunc(self):
        print(self.aaa + self.test())
        print('Do something...%sです' %self.aaa)
    def test(self):
        return "これはtestメソッドです."
    @classmethod
    def sample(self):
        return "bええええええええええええええb"
aa = MySampleClass()
aa.myfunc()
print("a")
aa = "cc"
print("%sです" %aa)

print(MySampleClass.sample())
