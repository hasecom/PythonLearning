import os
class Route:
    @classmethod
    def search(self,path):
        temp = (os.environ["REQUEST_URI"]).split('/')
        route = ""
        isRoute = False
        for name in temp:
            if isRoute:
                route += "/"+name
            if name == path:
                isRoute = True
        return route
        