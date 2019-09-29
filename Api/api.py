from Views import index
from App.Controllers import TopController
from datetime import datetime
class Api:
    @classmethod
    def first(cls):
        data = {
            "aa":"1",
            "bb":"2"
            }
        obj = ''
        f = open('App/Yields/index.html')
        html = f.read()
        f.close()
        obj += html %{'cnt':datetime.now().strftime("%Y/%m/%d %H:%M:%S")}
        return (index.Index()).view(obj)