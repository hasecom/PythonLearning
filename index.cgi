#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
import sys,io,cgi
import os
from App import config as c
from Routes import route,web
print("Content-type: text/html; charset=utf-8")
print("")

#URLのルーティング処理を行います。
route = route.Route.search(c.Conf.OpenEnv("DOMAIN")) #現在アクセスしているルーティングの取得
#ルーティンにあったファイルを出力します。
print(web.url[route])