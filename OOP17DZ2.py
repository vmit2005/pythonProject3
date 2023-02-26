import requests
from bs4 import BeautifulSoup
import csv


def csv_savng(name_csv, name_list):
    with open(name_csv, mode='w', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\r")
        for row in name_list:
            writer.writerow(row)
            print(row)


def main():
    req = requests.get("https://zastavok.net/").text

    soup = BeautifulSoup(req, "lxml")
    s = soup.find("div", class_="main")
    s1 = soup.find_all('div', class_="short_full")
    scrap = [['Описание картинки'.ljust(50, ' '), 'Ссылка на маленькую картинку : '.ljust(50, ' '),
              'Cсылка на картинку в полном формате : '.ljust(50, ' ')]]
    for i in s1:
        # print(i)
        #     print("Описание катринки : "+i.find('a').get('title'))
        name = str(i.find('a').get('title')).ljust(50, ' ')
        # print("Ссылка на маленькую картинку : "+"https://zastavok.net"+i.find('img').get('src'))
        src1 = str("https://zastavok.net" + i.find('img').get('src')).ljust(50, ' ')
        url = "https://zastavok.net" + (i.find('a').get('href'))
        # print(url)
        req1 = requests.get(url).text
        soup1 = BeautifulSoup(req1, "lxml")
        # print("Cсылка на картинку в полном формате : https://zastavok.net"+soup1.find('a',id="orig_size").get('href'))
        src2 = str("https://zastavok.net" + soup1.find('a', id="orig_size").get('href')).ljust(50, ' ')
        # print()
        # print()
        scrap.append([name, src1, src2])
    csv_savng("zastavki.csv", scrap)


if __name__ == '__main__':
    main()
