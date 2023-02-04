from bs4 import BeautifulSoup
import lxml
import  re
import requests

r = requests.get('https://tolyatti.vseinstrumenti.ru/category/shtykovye-lopaty-6296/?filters=collection%253Aspecification-202970%253A5700')

soup=BeautifulSoup(r.text,"lxml")
print(soup)
row=soup.find('div', {"data-qa":"products-tile"})
print (row)
# for i in row:
#     print (i)