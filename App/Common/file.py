class File:
    @classmethod
    def open(cls,path):
        f = open(path)
        file = f.read()
        f.close()
        return file