from django.db import models

from main.models import MyModel


# Create your models here.
class LoginDao(MyModel):
    def loginCheck(self, loginlist):
        conn = self.myconn()
        cursor = conn.cursor()
        sql = "select name from members where id=:1 and pwd=:2"
        cursor.execute(sql, loginlist)
        res = cursor.fetchone()
        print(f"res = {res}")
        cursor.close()
        conn.close()
        return res