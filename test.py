#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import cgi
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Content-type: text/html; charset=utf-8")
print("")
print("aa")
HtmlData = """
<!DOCTYPE html>
<html lang="ja">
<head>
  <title>Hello World | python</title>
</head>
<body>
<h1>Hello world for Python</h1>
<h2>よろしくお願いします．</h2>
<div>bb</div>
</body>
"""
 
print(HtmlData)