import warnings as wr
wr.filterwarnings(action='ignore')
from bs4 import BeautifulSoup
import requests
from urllib import parse
import cx_Oracle as ora
import os
import math
import re

class homework1117:




    def mission1(self, searchValue):

        conn = ora.connect('ict01/ict01@192.168.0.17/xe')
        cursor = conn.cursor()
        create_table = """
                CREATE TABLE books(
                    books_num NUMBER PRIMARY KEY,
                    books_name VARCHAR2(255),
                    books_category VARCHAR2(255),
                    image VARCHAR2(255),
                    price VARCHAR2(255),
                    release_date VARCHAR2(255)
                )
                """
        create_seq = """
                CREATE SEQUENCE books_seq INCREMENT BY 1 START WITH 1
                """

        # 테이블을 만들 떄 항상 새로운 테이블로 시작
        try:
            cursor.execute(create_table)
            cursor.execute(create_seq)
        except ora.DatabaseError:
            print('해당 테이블이 존재 합니다. 삭제 후 새로운 테이블을 만듭니다.')
            cursor.execute('drop table books')
            cursor.execute("drop sequence books_seq")
            cursor.execute(create_table)
            cursor.execute(create_seq)
        print("-----------------------------------------")
        url = 'https://search.kyobobook.co.kr/search?keyword={}&page={}'
        furl = url.format(parse.quote(searchValue), '{}')  # 주소에 검색어 적용
        soup = BeautifulSoup(furl, 'html.parser')

        totalpage_cnt = math.ceil(
            int(soup.find('p', {'class': 'result_count'}).find('b', {'class': 'fc_green'}).text.replace(',', '')) / 20)

        for i in range(1, totalpage_cnt + 1):
            purl = furl.format(i)  # 주소에 page 번호 적용
            res = requests.get(purl)
            soup = BeautifulSoup(res.text, 'html.parser')

            name = soup.find('span', id=re.compile(r"cmdtName_.*")).text  # 책이름

            img = soup.find('div', {'class': 'prod_area horizontal'}).find('img')  # 책이미지
            if "data-kbbfn-bid" in img.attrs:
                img_link = f'https://contents.kyobobook.co.kr/sih/fit-in/200x0/pdt/{img.attrs["data-kbbfn-bid"]}.jpg'
            else:
                img_link = img.attrs['src']

            category = soup.find(class_='prod_category').text  # 카테고리 명

            price = soup.find(class_='val').text  # 가격

            date = soup.find(class_='date').text  # 출판 날짜

            mydata = (name, category, img_link, price, date)
            sql = 'insert into books values(books_seq.nextval,:1,:2,:3,:4,:5)'
            cursor.execute(sql, mydata)
            print(i)

        conn.commit()
        cursor.close()
        conn.close()

    def mission2(self, category):
        pass


home = homework1117()
home.mission1('python')