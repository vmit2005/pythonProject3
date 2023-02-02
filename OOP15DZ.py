import json

class Nation():
    def __init__(self):
        try:
            self.data = json.load(open('nation.json'))
            if self.data == "":
                self.data = {}
        except FileNotFoundError:
            self.data = {}

    def add_nation(self):
        n = input("Bведите название страны (с заглавной буквы):")
        c = input("Bведите название cтолицы (с заглавной буквы):")

        self.data.update({n: {'capital': c}})
        with open("nation.json", "w") as f:
            json.dump(self.data, f, indent=2)

    def __str__(self):
        s = ""
        for n in self.data:
            s += f"{n}-{self.data[n]['capital']}\n"
        return s

    def del_nation(self):
        while True:
            n = str(input("Bведите название страны (с заглавной буквы): \n"
                          "Или нажмите [enter]"))

            if n == '':
                break
            if self.data.get(n) is None:
                print(f"Страна {n}  в базе не найдена")
                continue
            else:
                self.data.pop(n)
                return n

    def edit_nation(self):
        n = self.del_nation()
        c = input("Bведите название cтолицы (с заглавной буквы):")
        self.data.update({n: {'capital': c}})
        with open("nation.json", "w") as f:
            json.dump(self.data, f, indent=2)

    def find_nation(self):
        while True:
            n = str(input("Bведите название страны (с заглавной буквы): \n"
                          "Или нажмите [enter]"))

            if n == '':
                break
            if self.data.get(n) is None:
                print(f"Страна {n}  в базе не найдена")
                continue
            else:
                return f"{n} - {self.data[n]['capital']}"


n1 = Nation()
while True:
    print("Выбор действия:\n"
          "1 - добавление данных\n"
          "2 - удаление данных\n"
          "3 - поиск данных\n"
          "4 - редактирование данных\n"
          "5 - просмотр данных\n"
          "6 - Завернение работы")
    try:
        a = int(input("Ввод"))
    except:
        a=7
    if a == 1:
        n1.add_nation()

    if a == 2:
        n1.del_nation()
        print("Информация о стране удалена")

    if a == 3:
        print(n1.find_nation())

    if a == 4:
        n1.edit_nation()

    if a == 5:
        print(n1)

    if a == 6:
        break

    continue
