#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import sys
import io

print("勉強になります")
class AAA:
    def test(self):
        print("<div>%s</div>" % self.message())
    def message(self):
        return "こんばんはんです。"