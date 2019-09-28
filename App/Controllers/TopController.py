from Views import index
from App.Database import connection as c
class TopController:
    @classmethod
    def Index(cls):
        obj = ''
        f = open('App/Yields/index.html')
        html = f.read()
        f.close()
        obj += html.format("あああ")
        return (index.Index()).view(obj)