from Views import index
class TopController:
    @classmethod
    def Index(self):
        return (index.Index()).view("bb")