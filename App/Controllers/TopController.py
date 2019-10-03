from Views import index
from App.Database import connection as c
from datetime import datetime
from App.Common import file as f
class TopController:
    @classmethod
    def Index(cls):
        question = c.Connection(
            """
            SELECT CGM.ID, CGM.CATEGORY_CODE,CGM.LANG_CODE,LNG.LANG_NAME,LNG.LANG_KIND
            FROM CATEGORY_MAPS CGM
            INNER JOIN LANG LNG ON LNG.LANG_CODE = CGM.LANG_CODE
            INNER JOIN CATEGORY CAT ON CAT.CATEGORY_CODE = CGM.CATEGORY_CODE
            WHERE CAT.CATEGORY_LEVEL = %s
            AND CGM.AUTHORIZE = 1""",{0}).data
        obj = ''
        html = f.File.open('Views/Yields/index.html')
        obj += html %{
            'cnt':datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'question':question[0]['LANG_NAME']}
        return (index.Index()).view(obj)