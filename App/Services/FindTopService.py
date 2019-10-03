from App.Database import connection as c

class FindTopServices:
    def FindQuestion(self):

        question = c.Connection(
        """
        SELECT CGM.ID, CGM.CATEGORY_CODE,CGM.LANG_CODE,LNG.LANG_NAME,LNG.LANG_KIND
        FROM CATEGORY_MAPS CGM
        INNER JOIN LANG LNG ON LNG.LANG_CODE = CGM.LANG_CODE
        INNER JOIN CATEGORY CAT ON CAT.CATEGORY_CODE = CGM.CATEGORY_CODE
        WHERE CAT.CATEGORY_LEVEL = %s
        AND CGM.AUTHORIZE = 1
        """,{0}).data
        
        return question
        
    