from django.db import models
import pandas as pd


# Create your models here.
def make_dfall():
    df_all = pd.DataFrame({'sno': ['A001', 'B001', 'A002', 'B002', 'A003', 'B003'],
                           'student': ['홍길동', '이순자', '왕서방', '영심이', '호철이', '가진이'],
                           'kor': [85, 95, 85, 80, 90, 75],
                           'eng': [90, 95, 95, 80, 65, 100],
                           'math': [85, 75, 75, 100, 70, 80]
                           })
    return df_all
