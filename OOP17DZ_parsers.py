import requests
from bs4 import BeautifulSoup

class Parsers:
    html=""
    res=[]

    def __init__(self,url,path):
        self.url=url
        self.path=path

    def get_html(self):
        req=requests.get(self.url).text
        self.html=BeautifulSoup(req,'lxml')

    def parsing(self):
        pg=self.html.find_all("section",class_="content wrap")
        print =(pg)