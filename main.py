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

#csv(Соmma Separated  Values )(переменные разделенные запятыми

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
from bs4 import BeautifulSoup
import  re

# def get_copywriter(tag):
#     whois=tag.find("div",class_="whois").text.strip()
#     if "Copywriter" in whois:
#         return tag
#     return None


def get_salary(s):
    pattern=r"\d+"
    res=re.search(pattern,s).group()
    # res=re.findall(pattern,s)[0]
    print(res)

f=open('index.html',encoding='utf-8').read()
soup=BeautifulSoup(f,"html.parser")
# copywriter=[]
# row=soup.find_all('div',class_="row")
# for i in row:
#     cw=get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print (copywriter)


# row=soup.find('div',class_="name").text
# row=soup.find_all('div',class_="name")
# print(row)
# for i in row:
#     print(i.text)
#
# row = soup.find_all('div', class_="row")[1].find("div",class_="links")
# # print(row)
# row=soup.find_all("div",{"data-set":"salary"})[2].text
# print(row)
# row=soup.find("div",string="Alena").find_parent(class_="row")
# print(row)
# row=soup.find("div",id="whois3").find_previous_sibling()
# print(row)

salary=soup.find_all("div",{"data-set":"salary"})
for i in salary:
    get_salary(i.text)
