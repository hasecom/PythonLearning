from Views import index
from App.Services import FindTopService
from datetime import datetime
from App.Common import file as f
import json
import sys

class TopController:
    @classmethod
    def Index(cls,form = "None"):
        findTopSer = FindTopService.FindTopServices()
        q = findTopSer.FindQuestion()
        data   = sys.stdin.read()
        obj = ''
        html = f.File.open('Views/Yields/index.html')
        obj += html %{
            'cnt':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'question':q[0]['LANG_NAME'],
            'params':form}
        return (index.Index()).view(obj)