import os
import json
class Conf:
    @classmethod
    def OpenEnv(cls,key):
        f = open('.env')
        env = f.read()
        f.close()
        temp = env.split('\n')
        envDir = dict(s.split('=') for s in temp)
        return envDir[key]