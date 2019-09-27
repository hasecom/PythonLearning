#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-type: text/html; charset=utf-8")
print("")
print("a")