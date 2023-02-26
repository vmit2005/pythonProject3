def add_title(title):
    def wrapper(func):
        def wrap(*args,**kwargs):
            print(f"{title}".center(50,chr(9552)))
            output=func(*args,**kwargs)
            print(chr(9552)*50)
            print("")
            return output
        return wrap
    return wrapper

class UserInterface:
    @add_title('ВВод пользовательских данных')
    def wait_user_answer(self):
        # print("Ввод пользовательских данных".center(50, "="))
        print("Действия со статьями")
        print(" 1 - Создание статьи"
              "\n 2 - Просмотр статей"
              "\n 3- Просмотр определенной статьи"
              "\n 4- Удаление статьи"
              "\n q - выход из программы")
        user_answer = str(input("Выберите вариант действия: "))
        # print(user_answer)
        # print("=" * 50)
        return user_answer
    @add_title('Cоздание статьи')
    def add_user_article(self):
        dict_article = {
            "Название": None,
            "Автор": None,
            "Количество страниц": None,
            "Описание": None
        }
        # print("Создание статьи")
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи")
        # print("=" * 50)
        return dict_article

    @add_title('Список статей')
    def show_all_articles(self, articles):
            # print("Cписок статей: ".center(50, "="))

            for ind, article in enumerate(articles, start=1):
                print(f"{ind}. {article}")
            # print("=" * 50)
  # "  def add_title(title):"

    def get_user_article(self):
        user_article=input("BBедите название статьи")
        return user_article

    @add_title('Просмотр выбранной статьи')
    def show_single_article(self,article):
        for key in article:
            print(f" {key} cnfnmb {article[key]}")

    @add_title('Сообщение об ошибке')
    def show_incorrect_title_eror(self,user_title):
        print(f"Cтатьи с названием {user_title} не существует")

    @add_title('Удаление статьи')
    def remove_single_article(self,article):
        print(f"Статья {article}-была удалена")

    @add_title('Сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")