from OOP17DZ_parsers import Parsers
import requests
from bs4 import BeautifulSoup

def main():
    pars=Parsers("https://www.gismeteo.ru/weather-tolyatti-4429/","gsm.txt")
    print(pars)
    # pars.get_html()
    # print(pars.html())
    pars.parsing()
if __name__=='__main__':
    main()