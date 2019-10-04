from Views import index
from App.Controllers import TopController
import cgi

class Api:
    obj = None
    @classmethod
    def first(cls):
        form = cgi.FieldStorage()
        cls.obj = TopController.TopController.Index(form)
        return (index.Index()).view(cls.obj)