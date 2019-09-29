from Views import index
from App.Controllers import TopController

class Api:
    obj = None
    @classmethod
    def first(cls):
        cls.obj = TopController.TopController.Index()
        return (index.Index()).view(cls.obj)