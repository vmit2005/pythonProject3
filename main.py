# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
# # print(todos[:10])
# # print(type(todos))
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
# print(todos_by_user)
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
# print(f"User{s} {max_users} copleted {max_complete} TOdos")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count=str(todo['userId']) in users
#     return  is_complete and has_max_count
#
# with open('filtred_data_file.json','w') as f:
#     filtred_todos=list(filter(keep,todos))
#     json.dump(filtred_todos,f,indent=2)
#
# with open('filtred_data_file.json','r') as f:
#    data=json.load(f)
#    print(data)

# csv(Соmma Separated  Values )(переменные разделенные запятыми

#
# import csv
#
# with open ("data.csv","r",encoding="utf-8") as r_file:
#     file_reader=csv.reader(r_file,delimiter=";")
#     count=0
#     for row in file_reader:
#         if count==0:
#             print(f"Файл содержит столбцы {', '.join(row)}  ")
#         else:
#             print(f"  {row[0]}  {row[1]}.Родился {row[2]}")
#         count+=1
#     print(f'Всего строк в файле {count}')
#

import csv

# with open ("data.csv","r",encoding="utf-8") as r_file:
#     field_names=['имя', 'профессия','год рождения']
#     file_reader=csv.DictReader(r_file,delimiter=";",fieldnames=field_names)
#     count=0
#     for row in file_reader:
#         print(row)
#         if count==0:
#             print(f"Файл содержит столбцы {', '.join(row)}  ")
#         else:
#             print(f"  {row['имя']}.  {row['профессия']}.Родился {row['год рождения']}")
#         count+=1
#     print(f'Всего строк в файле {count}')

# with open('student.csv',mode='w', encoding="utf-8") as f:
#     writer = csv.writer(f, delimiter=',',lineterminator="\r")
#     writer.writerow(["Имя","Класс","Возраст"])
#     writer.writerow(['Женя','9','15'])
#     writer.writerow(['Саша','5','12'])
#     writer.writerow(['Маша','11','18'])
#

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open("data_sw.csv",mode='w', encoding="utf-8") as f:
#     writer=csv.writer(f,delimiter=",",lineterminator="\r")
#     for row in data:
#         writer.writerow(row)

# with open('data_sw.csv',mode="w") as f:
#    file_writer = csv.DictWriter(f, delimiter=",", lineterminator="\r",fieldnames=names)
#    file_writer.writeheader()
#    file_writer.writerow({"Имя:Cаша","Возраст":"6"})
#
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
# with open('dictwriter.csv','w')as f:
#     writer=csv.DictWriter(f,delimiter=";",lineterminator="\r",fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
#
# Парсинг
# from bs4 import BeautifulSoup
# import  re
#
# # def get_copywriter(tag):
# #     whois=tag.find("div",class_="whois").text.strip()
# #     if "Copywriter" in whois:
# #         return tag
# #     return None
#
#
# def get_salary(s):
#     pattern=r"\d+"
#     res=re.search(pattern,s).group()
#     # res=re.findall(pattern,s)[0]
#     print(res)
#
# f=open('index.html',encoding='utf-8').read()
# soup=BeautifulSoup(f,"html.parser")
# # copywriter=[]
# # row=soup.find_all('div',class_="row")
# # for i in row:
# #     cw=get_copywriter(i)
# #     if cw:
# #         copywriter.append(cw)
# #
# # print (copywriter)
#
#
# # row=soup.find('div',class_="name").text
# # row=soup.find_all('div',class_="name")
# # print(row)
# # for i in row:
# #     print(i.text)
# #
# # row = soup.find_all('div', class_="row")[1].find("div",class_="links")
# # # print(row)
# # row=soup.find_all("div",{"data-set":"salary"})[2].text
# # print(row)
# # row=soup.find("div",string="Alena").find_parent(class_="row")
# # print(row)
# # row=soup.find("div",id="whois3").find_previous_sibling()
# # print(row)
#
# salary=soup.find_all("div",{"data-set":"salary"})
# for i in salary:
#     get_salary(i.text)
#
#
# import requests
# from bs4 import BeautifulSoup
# import re

# r=requests.get("https://ru.wordpress.org")
# # print(r.headers)
# # print(r.headers['Content-Type'])
# # print(r.content)
# print(r.text)
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = "https://ru.wordpress.org"
#     print(get_data(get_html(url)))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header",id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# if __name__ == '__main__':
#     main()
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     print(get_data(get_html(url)))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section",class_="plugin-section")[3]
#     plugins=p1.find_all('article')
#     # return len(plugins)
#     for plugin in plugins:
#         name=plugin.find("h3").text
#         url=plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span",class_="rating-count").find("a").text
#
#         print(name,url,rating)
#
#
# if __name__ == '__main__':
#     main()
#
#
#
# from parsers import Parsers
# import requests
# from bs4 import BeautifulSoup
#
# def main():
#     pars=Parsers("https://www.ixbt.com/live/index/news/","new.txt")
#     pars.run()
#
#
# if __name__=='__main__':
#     main()
#
#
#
# MVC
# Model (модель)
# Viev (вид или представления)
# Controller(контроллер)
#
#
#
# Базы данных
# таблица состоит из столбцов(поля, атрибуты)
# строки (записи, кортежи)
# sqlite
import sqlite3 as sq

# con = sq.connect('profile.db')
# cur = con.cursor()
#
# cur.execute("""""")
# con.close()

# *.db, *.db3, *.sqlite, *.sqlite3

# with sq.connect('profile.db') as con:
#     cur=con.cursor()
#     cur.execute("""CREATE TABLE IF  NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data BLOB
#     )""")

# with sq.connect('users.db') as con:
#     cur=con.cursor()
#     cur.execute(
#         """
#         CREATE TABLE IF NOT  EXIST person(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         phone BLOB NOT NULL DEFAULT '+79090000000'
#         age  INTEGER  NOT NULL CHEK(age>15 AND age<70)
#         email TEXT UNIQUE
#         ALTER TABLE person rename to person_table
#         RENAME COLUMN addres TO home_adress
#         """
#     )

    # cur.execute("""CREATE TABLE IF  NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB  non nul DEFAULT '+79090000000',
    # age INTEGER NOT NULL CHECK(age>15 and age<70)
    # )""")
    # ADD
    # COLUMN
    # addres
    # TEXT
    # NOT
    # NULL
    # DEFAULT
    # "street"

with sq.connect('db_3.db') as con:
        cur=con.cursor()
        cur.execute("""
        SELECT * from T1
        order by FName
        LIMIT 2, 5
        """)
        res=cur.fetchone()
        print(res)
        # res2=cur.fetchmany(3)
        res2=cur.fetchall()
        print(res2)
        # for res in cur:
        #     print (res)

#Разработчики логической БД
#Разработчики физической БД
