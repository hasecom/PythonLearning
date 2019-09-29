from Views import index
from App.Database import connection as c
from datetime import datetime
from App.Common import file as f
class TopController:
    @classmethod
    def Index(cls):
        obj = ''
        html = f.File.open('Views/Yields/index.html')
        obj += html %{
            'cnt':datetime.now().strftime("%Y/%m/%d %H:%M:%S"
            )}
        return (index.Index()).view(obj)