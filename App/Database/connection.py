import pymysql.cursors
from App import config as c

class Connection:
    data = []
    def __init__(self, sql, val = None):
        connection = pymysql.connect(host=c.Conf.OpenEnv("DB_HOST"),
                    user=c.Conf.OpenEnv("DB_USER"),
                    password=c.Conf.OpenEnv("DB_PASS"),
                    db=c.Conf.OpenEnv("DB_NAME"),
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute(sql,val)
            dbdata = cursor.fetchall()
        self.data = dbdata
                    
        connection.close()