from Views import index
from App.Database import connection as c
from datetime import datetime
class TopController:
    @classmethod
    def Index(cls):
        obj = ''
        f = open('App/Yields/index.html')
        html = f.read()
        f.close()
        obj += html %{'cnt':datetime.now().strftime("%Y/%m/%d %H:%M:%S")}
        return (index.Index()).view(obj)