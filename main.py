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

# with sq.connect('db_3.db') as con:
#         cur=con.cursor()
#         cur.execute("""
#         SELECT * from T1
#         order by FName
#         LIMIT 2, 5
#         """)
#         res=cur.fetchone()
#         print(res)
#         # res2=cur.fetchmany(3)
#         res2=cur.fetchall()
#         print(res2)
#         # for res in cur:
#     print (res)

# Разработчики логической БД
# Разработчики физической БД
import sqlite3 as sq
# cars=[
#         ('BMV',54000),
#         ('Chevrolet',56000),
#         ('Daewo0',38000),
#         ('Citroen',29000),
#         ('Honda',33000)
#
#
# ]
# with  sq.connect('cars.db') as con:
#         cur = con.cursor()
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS cars(
#             car_id  INTEGER PRIMARY KEY AUTOINCREMENT,
#             model TEXT,
#             price INTEGER)
#                """)


# for car in cars:
#     cur.execute("INSERT  INTO cars VALUES(NULL,?,?)",car)

# cur .execute("INSERT  INTO cars VALUES(1,'Renault',20000)")
# cur .execute("INSERT  INTO cars VALUES(2,'Volvo',29000)")
# cur .execute("INSERT  INTO cars VALUES(3,'Mersedes',57000)")
# cur .execute("INSERT  INTO cars VALUES(4,'Bentley',35000)")
# cur .execute("INSERT  INTO cars VALUES(5,'Audi',52000)")
#
# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = Price+100;
# """)

#         cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price':0})
# cur.executemany("INSERT INTO cars VALUES(NULL,?,?)", cars)
#
#
#


# con = None
# try:
#     con = sq.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY key AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         );
#         BEGIN;
#         INSERT INTO cars VALUES (NULL, 'Renault',20000);
#         UPDATE cars SET price=price+100;
#
#         """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f"Ошибка выполнения запроса {e}")
# finally:
#     if con:
#         con.close()

# with sq.connect('cars.db') as con:
#     con.row_factory=sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#        car_id INTEGER PRIMARY key AUTOINCREMENT,
#        model TEXT,
#        price INTEGER
#     )
#     """)
#     cur.execute('SELECT model, price FROM cars')
#
#     for res in cur:
#         print (res['model'],res['price'])


# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png",'rb') as f:
#             return f.read()
#     except IOEror as e:
#         print(e)
#         return False
#
# with sq.connect('cars.db') as con:
#     con.row_factory=sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#        ava BLOB
#
#     """)
#     img=read_ava(1)
#     if img:
#         minary=sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES(?,?)",(1,binary))

# with sq.connect('cars.db') as con:
#
#     cur = con.cursor()
#     # with open('sql_dump.sql','w') as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open('sql_dump.sql','r') as f:
#         sql = f.read()
#         cur.executescript(sql)

##
##
# Шаблонизатор (Jinja)
from jinja2 import Template
#
#
# name="Игорь"
# age=28
# per = {'name': "Игорь", 'age': 28}
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# per = Person("Игорь", 26)
# #
# # # tm=Template("Mне {{a*2}} лет. Меня зовут {{name.upper()}}.")
# # # tm = Template("Mне {{p.age}} лет. Меня зовут {{p['name'].upper() }}.")
# # # tm = Template("Mне {{p.age}} лет. Меня зовут {{p['name'].upper() }}.")
# tm = Template("Mне {{p.get_age()}} лет. Меня зовут {{p.get_name() }}.")
# msg = tm.render(p=per)
# print(msg)
# # {{ }}-выражение для вставки констукции Pyton в if,kjy
# # {% %}-Спецификатор шаблона
# #
# # {%for <dshf;tybt>%}
# #     <тело цикла>
# # {%endfor%}

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Cмоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ярославль'},
#     {'id': 5, 'city': 'Уфа'}
# ]
# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id>3 %}
# <option value="{{c['id']}}" > {{c.city}}</option>
# {% elif c.city == 'Москва' -%}
#     <option  > {{c.city}}</option>
# {% else %}
#     {{c.city}}
# {% endif %}
# {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
#
#
# cities = [
#     {'id':'/index','title': 'Главная'},
#     {'id':'/news','title':'Новости'},
#     {'id':'/about','title': 'О коммпании'},
#     {'id':'/shop','title': 'Магазин'},
#     {'id':'/contact','title': 'Контакты'},
# ]
# link = """<ul>
# {% for c in cities -%}
# {% if c.title=='Главная' -%}
# <li><a href="{{ c.id }}" class="active">{{c.title}}</a></li>
# {% else -%}
# <li><a href="{{ c.id }}">{{c.title}}</a></li>
# {% endif -%}
# {% endfor -%}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)

# ОТ МАРИИ menu = [    {'id': 'index', 'title': 'Главная'},    {'id': 'news', 'title': 'Новости'},    {'id': 'about', 'title': 'О компании'},    {'id': 'shop', 'title': 'Магазин'},    {'id': 'contacts', 'title': 'Контакты'},]link = """<ul>{%for i in menu -%}{%if i.title=='Главная'-%}<li><a href="/{{i.id}}" class="active">{{i.title}}</li>{%else-%}<li><a href="/{{i.id}}">{{i.title}}</li>{%endif-%}{%endfor-%}</ul>"""tm = Template(link)msg = tm.render(menu=menu)print(msg)

# cars = [    {'model': 'Audi', 'price': 23000},
#             {'model': 'Skoda', 'price': 17300},
#             {'model': 'Renault', 'price': 44300},
#             {'model': 'Wolksvagen', 'pri<li><a href="{{ c.id }}">{{c.title}}</a></li>ce': 21300}]
# lst=[1,2,3,4,5]
# print(sum(map(lambda x: x['price'], cars)))
# tp1 = "Суммарная цена автомобилей {{ cs|sum(attribute='price') }}"
# tp1 = "Суммарная цена автомобилей {{ (cs|max(attribute='price')).model }}"
# tp1 = "Суммарная цена автомобилей {{ (cs|random) }}"
# tp1 = "Суммарная цена автомобилей {{ (cs|replace('model','brand')) }}"
#
#
# tm = Template(tp1)
# msg = tm.render(cs=cars)
# print(msg)
# tp2= "Суммарная цена автомобилей {{ ls | sum }}"
#
# tm2 = Template(tp2)
# msg2= tm2.render(ls=lst)
# print(msg2)
# sum1=0
# # map(sum,cars[''])
# for i in cars:
#     sum1 += i['price']
# print(sum1)
#
# print(sum(map(lambda x: x['price'], cars)))
#
# Макроопределения
# html="""
# {% macro input(name,value='', type='text', size=20) %}
#     <input type='{{type}}' name='{{name}}' value='{{value}}' size='{{size}}
# {% endmacro %}
# <p>{{input ('username','Ann')}}</p>
# <p>{{input ('email')}}</p>
# <p>{{input ('password',type='password')}}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)
#
# html="""
# {% macro input(name,placeholder='', type='text') -%}
#     <input type='{{type}}' name='{{name}}' placeholder='{{ placeholder }}' >
# {% endmacro %}
# <p>{{input ('firstname','Имя')}}</p>
# <p>{{input ('lastname','Имя')}}</p>
# <p>{{input ('address','Имя')}}</p>
# <p>{{input ('phone',type='tel',placeholder='Телефон') }}</p>
# <p>{{input ('email','Почта','email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)
#
#
#
# persons = [    {"name": "Алексей", "year": 18, "weight": 78.5},
#                {"name": "Никита", "year": 28, "weight": 82.3},
#                {"name": "Виталий", "year": 33, "weight": 94.0}]
#
# html='''
# {% macro list_users(list_of_users) %}
# <ul>
# {% for u in list_of_users  %}
#     <li>{{u.name}}{{ caller(u)}}</li>
# {%endfor%}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
# <ul>
#     <li> {{ user.year }}</li>
#     <li> {{ user.weight }}</li>
# </ul>
# {% endcall %}
# '''
#
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)
from jinja2 import Environment, FileSystemLoader
persons = [    {"name": "Алексей", "year": 18, "weight": 78.5},
               {"name": "Никита", "year": 28, "weight": 82.3},
               {"name": "Виталий", "year": 33, "weight": 94.0}]
subs=['культура','Наука','Политика','Спорт']


file_loader=FileSystemLoader('templates')
env=Environment(loader=file_loader)
tm=env.get_template('about.html')
msg=tm.render(list_table=subs)
print(msg)
#
#
#
# Flask микрофреймверк
# pip install flask

