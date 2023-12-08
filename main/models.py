from django.db import models
import cx_Oracle as ora

# Create your models here.
# Connection, 딥러닝모델, static[이미지, css, js],.... etc
class MyModel:
    def myconn(self):
        conn = ora.connect('ict01/ict01@192.168.0.17/xe')
        return conn